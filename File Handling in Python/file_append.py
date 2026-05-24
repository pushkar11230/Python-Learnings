a = "\nThis line will also add in the sample text file"

file = open("sample.txt", "a")
file.write(a)

file.close()
