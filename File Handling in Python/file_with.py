a = "\nThis is a sample text added through 'with'"

# file = open("sample.txt", "a")
# file.write(a)
# file.close()

with open("sample.txt", "a") as file:
    file.write(a)