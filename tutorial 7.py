# Date 13-3-2021
# In this tutorial we will learn about variables Escape characters input command and many more
# p standa for paragraph
p = "My name is Aman, I study in class 9 in St. Paul\'s School "
# Now if we will print p then see the result
print(p)


counter = 100  # An integer assignment
miles = 1000.75  # A floating point
name = "Aman"  # A string
counter2 = "98"  # Also a string because it is written in double quote
counter3 = "43"  # Also a string because it is written in double quote

# The downer syntax will print that which type of variable are these
print(type(counter))
print(type(miles))
print(type(name))
# The upper syntax will print that which type of variable are these


# The downer syntax will print that which type of variable are these
print(p+name)  # It will print
# My name is Aman, I study in class 9 in St. Paul\'s School Aman
# Same like upper syntax if we write
print(counter+miles)
# then it will print their addition

# In this (downer) case counter2 and counter3 is in double quote so it is an string but in any case if it is a integer or a floating point number then the downer syntax will give you an error
print(p+counter2)
print(counter2+counter3)

# In the downer syntax I had converted string value into a integer value
print(int(counter2)+int(counter3))
# Similary, like int() you can also use str(), float() etc. for Type Casting

# The downer syntax show you that how to print 10 lines with a same print command
print(10*"Hello World!\n")

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

# Now we will learn about Input command
print("Enter a number of which you want to know +10 of entered number")
num1 = input()
print("+10 of your number is",10+int(num1))
