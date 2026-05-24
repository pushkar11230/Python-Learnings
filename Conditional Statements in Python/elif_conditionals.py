marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: F")

if marks % 2 == 0:
    print("Your marks is even!")
else:
    print("Your marks is odd!")
