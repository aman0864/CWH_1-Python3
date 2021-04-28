# Date 18-3-2021

# In this tutorial we will discuss about python built in functions
# And we will also make our own functions in Python


print("Enter the value of A")
a = float(input())
print("Enter the value of B")
b = float(input())

c = sum((a, b))  # This i.e. sum is an example of built in functions
print(c)
print(10*"\n")


def func1(x, y):  # An example of user defined function
    """This function will ask input from the user and it will also calculate the average of user input values"""
    z = (x+y)/2
    return z  # this line is important to get result in any variable


print("Enter the value of X")
x = float(input())
print("Enter the value of Y")
y = float(input())
out = func1(x, y)  # this line is important to get result in any variable
print(out)
print(func1.__doc__)  # Used to print the doc string of any particular function
# Doc string is the first line of any function
