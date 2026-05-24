def greet():
    print("Good Morning")
    print("How are you")
    print("Thank you")


greet()


def greet_2(name):
    print(f"Hello {name}, how are you?")


greet_2("Pushkar")


def add(a, b):
    print(a + b)

add(4, 7)
add("Pushkar ", "Bhadani")



def add_2(a, b):
    # print(a + b)
    return a + b

c = add_2(6, 4)
print(c)



def total(*args): 
    print(args)


total(1, 2, 3, 4) 


def user_details(**kwargs): 
    print(kwargs) 

user_details(name="Harry", age=25)



