# Teplova // Create a variable with a dictionary, use {}, output it
my_dict = {"Agafonov":  350000, "Brekunov": 1200000, "Chern": 568000}
print(my_dict)
print(my_dict.items())
# output one existing value of the dictionary, one - non-existent value
print(my_dict["Chern"])
print(my_dict.get("Chern"))
#print(my_dict["Ivanov"])
print(my_dict.get("Ivanov"))
# Add two values, don't forget to use {}
my_dict.update({"Tsvetkova": 10000, "Semenova": 20})
print(my_dict)
print(my_dict.items())
my_dict["Kuzovlev"] = 5000
print(my_dict)
print(my_dict.items())
# Delete one value and output this value
a = my_dict.pop("Kuzovlev")
print(my_dict)
print(my_dict.items())
print(a)
# Create a variable with different type data. Output it
my_set = {54, 85, 6, 85 ,8 ,6 , "o", "g", "d", "o", "7", (5, 6, 5), (5, 8) , (5, 6, 5) }
print(my_set)
# Add two elements and output it
my_set.update("w")
my_set.add(70)
print(my_set)
# delete the element
a = my_set.remove(85)
b = my_set.remove("d")
print(my_set)
d = my_set.discard((5, 6, 5))
print(my_set)
# the first element was deleted
my_set = {54, 85, 6, 85 ,8 ,6 }
my_set.pop()
print(my_set)
