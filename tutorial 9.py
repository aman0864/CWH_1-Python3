# Date 14-3-2021

# Making a alphabetic list
str1 = ["Box", "Penceil", "Pen", "Eraser", "Sharpner", "Protactor"]

# Making a numeric list
str2 = ["43", "2", "76", "0", "89", "3"]
# You can also enter the numeric values without double Quote

print(5*"\n")
# The below syntax will arrange the str1 in acesinding order
str1.sort()
# Rember: If you use sort or reverse type functions then the main value of list will also change

print(5*"\n")
# The below syntax will arrange the str1 in reverse order
str1.reverse()
# Rember: If you use sort or reverse type functions then the main value of list will also change
print(str1)

print(5*"\n")
# The below syntax will arrange the str2 in acesinding order
str2.sort()
# Rember: If you use sort or reverse type functions then the main value of list will also change

print(5*"\n")
# The below syntax will arrange str2 in reverse order
str2.reverse()
# Rember: If you use sort or reverse type functions then the main value of list will also change
print(str2)

print(5*"\n")
print(10+int(str2[2]))

print(5*"\n")
# Now let's discuss about some other string functions
# Let's create a list first
str3 = [58, 87, 23, 1, 0, 5, 78, 36, 45, 2]

print(5*"\n")
# First we will discuss about append function this function adds a variable in the end of the list
str3.append(84)
print(str3)
# See this append function has added 84 in the end of the list


print(5*"\n")
# Now let's discuss about insert function this function adds a variable in the indes given to it of the list
str3.insert(4, "Aman")
print(str3)
# See this insert function has added Aman in the index given of the list


print(5*"\n")
# Now let's discuss about pop function this function removes the last value of the list
str3.pop()
print(str3)
# See the 84 is again removed


print(5*"\n")
# Now let's discuss about remove function this function removes the given value from the list
str3.remove("Aman")
print(str3)
# See the Aman is removed


print(5*"\n")
# Now let's discuss about Tuple
# Tuple is nothing but the list which cannot be change
# To make a Tuple use this syntax
tuple1 = (1, 12, 46, 76, 0, 56)
# Now if you will try to change the value of tuple by any command such as 
# tuple1.pop()
# tuple1.remove(12)
# It will give you an Error

# But if you write the below syntax it will not give you an Error
# print(tuple1.count(56))
