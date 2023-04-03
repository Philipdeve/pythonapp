# Lists are an essential Python data structure.
# The allow you to group together multiple values and reference them all with a
# common name.

items = ["Roger", 1, "Syd", True]
print(items[1])

print("Roger" in items) 

len(items) 

items[2] = "John"

items.append("Test")

items.insert(1, "Tea") 
items[1:1] = ["Test1", "Test2"]

items.remove("Test")

print(items)

animals = ["cat", "alligator", "dog", "frog", "Frog"]
#animals.sort()
animals.sort(key=str.lower) #sorts in lowercase
print(animals)