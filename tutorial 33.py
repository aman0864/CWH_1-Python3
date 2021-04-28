# Date 19-3-2021

# In this tutorial we will learn about local and global variables in python

x = 1  # An example of Global Variable
"""
def func1():
    x+=1
    print(x)

func1()
"""

# The upper syntax will surely give you an error because value of a global variable cannot be changed in a function


# To change the value of a global variable in a function use the below syntax

def func2():
    global x  # Asking permission to change the value of x
    x += 1
    print(x, "Is a Global Variable, but global function has asked permission from Python to change it's value ")


func2()

