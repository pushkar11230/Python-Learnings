# 1. Create a function that prints "Hello World".

def hw():
    print("Hello World!")

# hw()

# 2. Create a function that takes a name and prints:  "Hello, Pushkar".


def welcome(name):
    print("Hello,", name)

# welcome("Pushkar")


# 3. Create a function that takes two numbers and returns their sum.

def sum(a, b):
    return a+b

# print(sum(4, 4))



# 4. Create a function to find the square of a number.

def square(a):
    print(a**2)

# square(4)


# 5. Create a function to check whether a number is even or odd.

def evn_od(a):
    if a % 2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")

# evn_od(39)


# 6. Create a function that returns the largest of two numbers.

def largest(a, b):
    if a>b:
        print(a, "is larger")
    else:
        print(b, "is larger")

# largest(48, 6)



# 7. Create a function that returns the smallest of three numbers.

def smallest(a, b, c):
    if a<=b and a<=c:
        print(a, "is the smallest")
    elif b<=a and b<=c:
        print(b, "is the smallest")
    elif c<=a and c<=b:
        print(c, "is the smallest")

# smallest(5,3,7)


# 8. Create a function that counts the length of a string without using len().

def length(str):
    a = 0
    for i in str:
        a += 1
    # print(f"The length of '{str}' is {a}")
    return a

# print(length("Calender"))



# 9. Create a function to calculate the factorial of a number.

def fact(a):
    f = 1
    for i in range(a):
        f = f * a
        a = a-1
    return f

# print(fact(6))


# 10. Create a function that checks whether a number is positive, negative, or zero.

def check_num(a):
    if a > 0:
        print(f"{a} is a positive number.")
    elif a == 0:
        print(f"{a} is zero.")
    elif a < 0:
        print(f"{a} is a negetive number.")
    
# check_num(0)


# 11. Create a function that prints numbers from 1 to n.

def ptr_till(a):
    for i in range(1, a+1):
        print(i)
    
# ptr_till(100)



# 12. Create a function that returns the sum of numbers from 1 to n.

def sum_till(a):
    b = 0
    for i in range(a+1):
        b = b + i
    return b

# print(sum_till(5))



# 13. Create a function to print the multiplication table of a number.

def multiplication_table(a):
    for i in range(1,11):
        print(i*a)

# multiplication_table(5)


# 14. Create a function that counts vowels in a string.

def vowels(string):
    a = 0
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            a += 1
        elif i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            a += 1
    print(f"There are {a} vowels in {string}")

vowels("Pushkar")