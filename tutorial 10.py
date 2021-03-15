# Date 14-3-2021

# Now we will learn about python dictionary
dict1 = {"Aman": "Burger", "Rohan": "Pizza", "Suman": "Pasta"}
# Thus the dictionary nane dict1 is created
print(dict1)

# Use this syntax to add a word or two in any dictionary
print(5*"\n")
dict1["Ankit"] = "Ice Cream"
print(dict1)

# Use this syntax to delete a word or two in any dictionary
print(5*"\n")
del dict1["Rohan"]
print(dict1)

# Use this syntax to get the meaning of a word from a dictionary
print(5*"\n")
print(dict1["Suman"])

# Following are some python functions
print(5*"\n")
print(dict1.get("Aman"))
# used to know the meaning of a word in a dictionary 

print(5*"\n")
dict1.update({"Sorab":"Maggi"})
print(dict1)
# used to add a word or two in a dictionary 

print(5*"\n")
print(dict1.items())
# used to know all pairs in a dictionary 

print(5*"\n")
print(dict1.keys())
# used to know only words(i.e. like Aman, Sorab, Suman, etc.) in the dictionary a dictionary 

print(5*"\n")
# There is also more functions like .copy() (explained in tutorial 10 python) 
