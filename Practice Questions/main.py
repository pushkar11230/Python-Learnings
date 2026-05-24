'''
Print this

1
121
12321
1234321
123454321

'''

# n = 5
# for row in range(1, n + 1):

#     # Increasing numbers
#     for inc in range(row):
#         print(inc + 1, end="")
    
#     # Decreasing numbers
#     for dec in range(row - 1):
#         print(row - dec - 1, end="")
#     print()





# Find the second largest number in a list without using sort().

# numbers = [4, 7, 1, 9, 3, 4, 8, 10, 9, 6]

# largest = float('-inf')
# sec_largest = float('-inf')


# for num in numbers:
#     if num > largest:
#         sec_largest = largest
#         largest = num
#     elif num > sec_largest and num != largest:
#         sec_largest = num

# print(f"Second largest number is {sec_largest}")





# Character Frequency Counter

# word = "programming"

# frequency = {}

# for char in word.lower():
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# for key, value in frequency.items():
#     print(f"{key} : {value}")




# -----------------------X-----------------------------


# “If number is negative, print Negative Number.”

# num = -5 

# if num < 0:
#     print("Negative number")
# else:
#     print("Positive number")



# “Loop through every character in a string.”

# string = "Pushkar"
# for char in string:
#     print(char)



# “If character already exists in list, print Already Exists.”

# chars = ["a", "b", "f", "a", "s", "q", "f", "v", "v"]

# j = input("Enter the char: ")

# if j in chars:
#     print("Already exists")
# else:
#     chars.append(j)
    
# print(chars)




# “Keep asking user input until they type exit.”

# user_input = input("Enter: ")

# if user_input == "exit":
#     print("Closing...")
# else:
#     user_input = input("Enter: ")