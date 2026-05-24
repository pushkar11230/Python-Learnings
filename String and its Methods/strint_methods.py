name = 'Pushkar'

# name[0] = "T"  # Not allowed
print(name) 


# String Methods
print(len(name))
print(name.lower())
print(name.upper())
print(name)
name = name.upper()
print(name)


name2 = "   Pushkar   "

print(name2)
print(len(name2))
print(name2.strip())  # Removes the extra spaces in the string

print(len(name2.strip()))


text = "Victor is here"

print(text)
print(text.replace("Victor", "Doom"))


text2 = "Hello"
print(text2.isalpha())
print(text2.isnumeric())


num1 = "934"
print(num1.isnumeric())
print(num1.isalpha())


text3 = "Pushkar11230"
print(text3.isalnum())
