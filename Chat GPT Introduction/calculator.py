import tkinter as tk

# ---------------- WINDOW ---------------- #
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#1e1e1e")

# Allow window resizing
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

# ---------------- VARIABLES ---------------- #
expression = ""
input_text = tk.StringVar()

# ---------------- ENTRY ---------------- #
entry = tk.Entry(
    root,
    textvariable=input_text,
    font=("Arial", 24),
    bd=10,
    relief=tk.RIDGE,
    justify="right"
)

entry.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# ---------------- FUNCTIONS ---------------- #
def button_click(value):
    global expression

    expression += str(value)
    input_text.set(expression)


def clear():
    global expression

    expression = ""
    input_text.set("")


def calculate():
    global expression

    try:
        result = str(eval(expression))

        input_text.set(result)
        expression = result

    except:
        input_text.set("Error")
        expression = ""


# ---------------- BUTTON FRAME ---------------- #
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.grid(row=1, column=0, sticky="nsew")

# Make frame expandable
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for j in range(4):
    button_frame.columnconfigure(j, weight=1)

# ---------------- BUTTONS ---------------- #
buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "%", "="]
]

for row_index, row in enumerate(buttons):

    for col_index, button_text in enumerate(row):

        bg_color = "#ffffff"

        if button_text in ["+", "-", "*", "/"]:
            bg_color = "#ffa500"

        elif button_text == "=":
            bg_color = "#66cc66"

        elif button_text == "C":
            bg_color = "#ff6666"

        # Commands
        if button_text == "C":
            command = clear

        elif button_text == "=":
            command = calculate

        else:
            command = lambda value=button_text: button_click(value)

        # Button
        button = tk.Button(
            button_frame,
            text=button_text,
            font=("Arial", 18),
            bg=bg_color,
            command=command
        )

        # sticky="nsew" makes button stretch
        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=2,
            pady=2
        )

# ---------------- RUN ---------------- #
root.mainloop()

