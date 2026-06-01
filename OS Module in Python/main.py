import os 

if not os.path.exists("OS Module in Python/Data"):
    os.mkdir("OS Module in Python/Data")


for i in range(1, 101):
    if not os.path.exists(f"OS Module in Python/Data/Tutorial {i}"):
        os.mkdir(f"OS Module in Python/Data/Tutorial {i}")


folders = os.listdir("OS Module in Python/Data")

print(folders)
