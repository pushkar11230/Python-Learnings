import os
import shutil

FOLDER_PATH = os.getcwd()

FILE_TYPES = {
    "PDFs": [".pdf"],
    "Word_Files": [".docx", ".doc"],
    "Excel_Files": [".xlsx", ".xls", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".webp", ".gif"],
    "Videos": [".mp4", ".mkv"],
    "Document": [".txt", ".pdf"]
}

for folder in FILE_TYPES:
    if not os.path.exists(folder):
        os.mkdir(folder)

for file in os.listdir(FOLDER_PATH):
    if os.path.isdir(file):
        continue

    ext = os.path.splitext(file)[1].lower()

    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            shutil.move(file, os.path.join(folder, file))
            break
