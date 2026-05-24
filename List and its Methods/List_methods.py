fruits = ["Apple", "Banana", "Orange", "Grapes", "Watermelon"]

print(len(fruits))

fruits.append("Mango")  # Add an item at the last (Takes only one argument)
print(fruits)

fruits.insert(1, "Papaya")  # Add an item at the given index
print(fruits)


vegetables = ["Potato", "Tomato", "Onions"]

fruits.extend(vegetables)
print(fruits)

# vegetables.append("Olive", "Carrot")  # Error
print(vegetables)


vegetables.remove("Onions")
print(vegetables)


fruits.pop(4)
print(fruits)

fruits.pop()
print(fruits)

vegetables.clear()
print(vegetables)

print(fruits.index("Banana"))


surnames = ["Bhadani", "Gupta", "Bhadani", "Shah", "Bhadani"]

print(surnames.count("Bhadani"))


print("Gupta" in surnames)
