# Count Frequency of Words

# text = "python is easy and python is powerful"

# frequency = {}

# for word in text.split():
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# print(frequency)




# Find Second Largest Number

# numbers = [4, 8, 1, 9, 3, 9, 7]

# largest = float("-inf")
# sec_largest = float("-inf")

# for num in numbers:
#     if num > largest:
#         sec_largest = largest
#         largest = num
#     elif num < largest and num > sec_largest:
#         sec_largest = num
# # print("Largest:", largest)
# print("Second largest:", sec_largest)





# Check for Palindrome Sentence

# text = "A man a plan a canal Panama"

# n_text = text.lower().replace(" ", "")
# reversed_text = n_text[::-1]

# print(text)

# if n_text == reversed_text:
#     print("Palindrome")
# else:
#     print("Not Palindrome")




# Group Even and Odd Numbers

# numbers = [1, 2, 3, 4, 5, 6]

# even_odd = {
#     "Even": [],
#     "Odd": []
# }

# for num in numbers:
#     if num % 2 == 0:
#         even_odd["Even"].append(num)
#     else:
#         even_odd["Odd"].append(num)

# print(even_odd)




# Find Missing Numbers

# numbers = [1, 2, 3, 5, 6, 8, 10, 11, 12, 14]

# miss_nums = []

# for num in range(1, numbers[-1]):
#     if num not in numbers:
#         miss_nums.append(num)

# print(miss_nums)




# Remove Duplicate Characters From String

# text = "programming"

# new_text = ""

# for char in text:
#     if char not in new_text:
#         new_text += char
    
# print(new_text)





# Create a Simple Login System

# users = {
#     "pushkar": "1234",
#     "admin": "abcd",
#     "laptop": "1a2b"
# }

# user_id = input("Enter the ID: ")

# if user_id in users:
#     password = input("Enter the Password: ")
#     if users[user_id] == password:
#         print("\nLogin Successful!")
#     else:
#         print("\nWrong Password!")
# else:
#     print(f"\nNo ID found as '{user_id}'")




# Matrix Addition

# m1 = [
#  [1, 2],
#  [3, 4]
# ]

# m2 = [
#  [5, 6],
#  [7, 8]
# ]

# ''' 

# m1[0][0] m1[0][1]
# m1[1][0] m1[1][1]

# m2[0][0] m2[0][1]
# m2[1][0] m2[1][1]

# '''

# add = [
#     [],
#     []
# ]

# for i in range(len(m1)):
#     for j in range(len(m2)):
#         add[i].insert(j, m1[i][j] + m2[i][j])

# print(add[0])
# print(add[1])




# Find Most Frequent Element in List

numbers = [1, 2, 2, 3, 4, 2, 2, 5, 3, 3]

frequency = {}

for num in numbers:
    if num not in frequency:
        frequency[num] = 1
    else:
        frequency[num] += 1

largest = 0
most_frequent = None

for key in frequency:
    if frequency[key] > largest:
        largest = frequency[key]
        most_frequent = key

print(f"Most frequent number in the list is {most_frequent} which occured {largest} times.")
