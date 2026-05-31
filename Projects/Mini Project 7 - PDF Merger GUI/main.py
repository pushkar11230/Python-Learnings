import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter

os.chdir(os.path.dirname(__file__))


class PdfMergerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Merger GUI")
        self.geometry("520x360")
        self.resizable(False, False)

        self.pdf_list = []

        self._create_widgets()

    def _create_widgets(self):
        tk.Label(self, text="Selected PDF files:", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=12, pady=(12, 0))

        self.listbox = tk.Listbox(self, width=68, height=10, selectmode=tk.EXTENDED)
        self.listbox.pack(padx=12, pady=(4, 10))

        button_frame = tk.Frame(self)
        button_frame.pack(fill="x", padx=12)

        tk.Button(button_frame, text="Add PDFs", width=12, command=self.add_pdfs).pack(side="left")
        tk.Button(button_frame, text="Remove Selected", width=14, command=self.remove_selected).pack(side="left", padx=8)
        tk.Button(button_frame, text="Clear All", width=10, command=self.clear_all).pack(side="left")

        output_frame = tk.Frame(self)
        output_frame.pack(fill="x", padx=12, pady=(12, 0))

        tk.Label(output_frame, text="Output file name:").grid(row=0, column=0, sticky="w")
        self.output_entry = tk.Entry(output_frame, width=40)
        self.output_entry.grid(row=0, column=1, padx=(6, 0), pady=4)
        self.output_entry.insert(0, "merged.pdf")

        tk.Button(output_frame, text="Browse...", command=self.choose_output_path).grid(row=0, column=2, padx=6)

        merge_frame = tk.Frame(self)
        merge_frame.pack(fill="x", padx=12, pady=16)

        tk.Button(merge_frame, text="Merge PDFs", width=16, bg="#4CAF50", fg="white", command=self.merge_pdfs).pack()

        tk.Label(self, text="Select PDF files in the order you want them merged.", fg="#555555").pack(padx=12, anchor="w")

    def add_pdfs(self):
        file_paths = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf")],
            initialdir=os.getcwd(),
        )
        if not file_paths:
            return

        for path in file_paths:
            if path not in self.pdf_list:
                self.pdf_list.append(path)
                self.listbox.insert(tk.END, os.path.basename(path))

    def remove_selected(self):
        selected_indices = list(self.listbox.curselection())
        if not selected_indices:
            return
        for index in reversed(selected_indices):
            self.listbox.delete(index)
            self.pdf_list.pop(index)

    def clear_all(self):
        self.pdf_list.clear()
        self.listbox.delete(0, tk.END)

    def choose_output_path(self):
        output_path = filedialog.asksaveasfilename(
            title="Save merged PDF as",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile=self.output_entry.get() or "merged.pdf",
            initialdir=os.getcwd(),
        )
        if output_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, output_path)

    def merge_pdfs(self):
        if not self.pdf_list:
            messagebox.showwarning("No PDFs selected", "Please add at least one PDF file to merge.")
            return

        output_name = self.output_entry.get().strip()
        if not output_name:
            messagebox.showwarning("Invalid output name", "Please enter a valid output file name.")
            return

        output_path = output_name
        if not output_path.lower().endswith(".pdf"):
            output_path += ".pdf"

        try:
            merger = PdfWriter()
            for pdf in self.pdf_list:
                merger.append(pdf)
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged PDF saved as:\n{output_path}")
        except Exception as exc:
            messagebox.showerror("Merge failed", f"Could not merge PDFs:\n{exc}")


if __name__ == "__main__":
    app = PdfMergerApp()
    app.mainloop()