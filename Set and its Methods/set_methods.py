fruits = {"Apple", "Banana"}

fruits.add("Orange")
print(fruits)

fruits.update(["Mango", "Peach"])
print(fruits)

print(len(fruits))

fruits.remove("Banana")
print(fruits)

fruits.discard("oranges")  # No error
print(fruits)

fruits.pop()  # Removes a random item
print(fruits)


removed_fruit = fruits.pop()
print(removed_fruit)


fruits.clear()
print(fruits)
