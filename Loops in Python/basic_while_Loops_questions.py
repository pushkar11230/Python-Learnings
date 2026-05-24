# 1. Print numbers from 1 to 10 using while.

# i = 1
# while i<=10:
#     print(i)
#     i += 1


# 2. Print even numbers from 2 to 20.

# i = 2
# while i<=20:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# 3. Find the sum of first 10 natural numbers

# i = 1
# j = 0
# while i<=10:
#     j = j+i
#     i += 1
# print(j)


# 4. Keep printing numbers until the user enters 0

# i = int(input("Enter a number: "))
# while i != 0:
#     print(i)
#     i = int(input("Enter a number again: "))

# print("You entered 0")


# 5. Reverse a number using a loop. (Example: 1234 → 4321)

# num = input("Enter a number: ")

# while True:
#     reversed = num[::-1]
#     print(int(reversed))
#     break


# 6. Count digits in a number.

# i = input("Enter a number: ")
# while True:
#     print(len(i))
#     break


# 7. Find the sum of digits of a number. (Example: 123 → 1+2+3 = 6)

num = int(input("Enter a number: "))

sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits = sum_digits + digit
    num = num // 10

print("Sum of digits =", sum_digits)


# 8. Check whether a number is palindrome or not. (Example: 121 , 3443 , 12321 → Palindrome)

# num = int(input("Enter a number: "))

# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

