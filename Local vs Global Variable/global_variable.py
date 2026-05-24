x = 23
def func():
    print(x)

# func()
# print(x)


# Changing the global variable inside a function

a = 55
def show():
    global a
    a = 67 
    print(a)

show()
print(a)
