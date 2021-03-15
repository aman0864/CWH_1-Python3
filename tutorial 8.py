# Date 13-3-2021
# In this programe we will learn about string slicing and string functions

string1 = "My Name is Aman, I\'m a good boy!"
print(string1[14])
print(5*"\n")
# To give the new line 5 times
print(string1[0:15])

print(5*"\n")
string2 = "Who are you!"
print(len(string2))
print(string2[0:12])

print(5*"\n")
# use below function to print string by leaving some characters in between
print(string1[::2])
# Or you can also use
# print(len(string1[0:15:2]))
# for the same output

print(5*"\n")
# Use below syntax to print the given string in reverse order
print(string1[::-1])

print(5*"\n")
# Use below syntax to print the given string in reverse order with leaving some characters
print(string1[::-2])
# You can also use this
# print(string1[32:0:-2])
# to get the same output


print(5*"\n")
# Making a upper alphabet string
string3 = "Aman is a good boy"
# Making a lower alphabet string
string4 = "aman is a good boy"
print(string3.isalnum())
print(string3.isalpha())
print(string3.endswith("boy"))
print(string3.count("o"))
print(string4.capitalize())
print(string4.find("good"))
print(string3.lower())
print(string4.upper())
print(string4.replace("good", "best"))
