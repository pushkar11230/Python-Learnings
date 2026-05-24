student = {
    "Name": "Pushkar",
    "City": "Ranchi",
    "Language": "Python",
    "Age": 20,
    "College": "DSPMU",
    "Color": "Blue"
}

student.pop("College")
print(student)


student.popitem()  # Removes the last inserted key value pair
print(student)


del student["Age"]
print(student)


# student.clear()
# print(student)

print(student.keys())

print(student.values())

print(student.items())


student2 = dict(Name = "Aman Gupta", Company = "Boat")

print(student2)


# Adding multiple key value pairs at once
student2.update(
    {
        "Age": 45,
        "Class": "12th"
    }
)

print(student2)
