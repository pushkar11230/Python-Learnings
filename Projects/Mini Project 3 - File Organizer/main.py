import os
import shutil

# Folder path you want to organize
FOLDER_PATH = os.getcwd() # Current working directory

# File type mapping

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz']
}

# Create folders if they don't exist
for folder in FILE_TYPES.keys(): # Create folders for each file type category (Which is here is the key of the FILE_TYPES dictionary)
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for file_name in os.listdir(FOLDER_PATH):  # Loop through each file in the folder
    file_path = os.path.join(FOLDER_PATH, file_name)

    # Skip folders and the script itself
    if os.path.isdir(file_path):
        continue
    if file_name == os.path.basename(__file__):
        continue

    # Get file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    for folder, extensions in FILE_TYPES.items():
        if file_extension in extensions:
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder))
            break

print("Files have been organized successfully ✅")
