student = {
    "Name": "Pushkar",
    "City": "Ranchi",
    "Language": "Python"
}

print(student)
print(student["Language"])
print(student["City"])
print(student["Name"])



# print(student["Nameeee"])  # Error

print(student.get("Nameeeee"))  # No Error
print(student.get("Name"))
print(student.get("City"))


student["City"] = "Jamshedpur"
print(student)



# Another way to create a dictionary
student2 = dict(Name = "Aman Gupta", Company = "Boat")

print(student2)
print(type(student2))
