a = "My name is Pushkar"

# file = open("pushkar.txt", "w")
# file.write(a)

file = open("sample.txt", "r")
# content = file.read()
content = file.readlines()
print(content)

file.close()
