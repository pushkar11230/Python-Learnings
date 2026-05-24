# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# try:
#     print("The value of a/b is: ", a/b)
# except Exception as e:
#     print("Some error occured:", e)

# print("Thank you")




try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print(y)
except ZeroDivisionError:
    print("Division by zero is not allowed!")
except ValueError:
    print("Enter a valid number!")
finally:
    print("This line will always run")
    # 'finally' will always run even if we used return statement

print("Thank you")

