# Date 21-3-2021

# It this tutorial you will learn about python decorators

# in Python decorators a generally used to just modifiying a particular function without changing in it's main code


# def decorator(wswap):
#     # This functions is a decorator
#     global x
#     global y
#     if x < y:
#         x, y = y, x
#     wswap()
#     print("The output is two numbers diffrence which is already displayed:")


# def diffrence(x, y):
#     return x-y


# # print(diffrence(9, 4))
# # decorator(diffrence(2, 8))
# diffrence = decorator(diffrence)
# diffrence()


def decorator(func1):
    def will_execute():
        print("Executing now")
        # the upper print command will execute only before execution of the main function i.e. myname()
        func1()
        print("Execution finished")
        # the upper print command will execute only after the execution of the main function i.e. myname()
    return will_execute

@decorator
def myname():
    print("My name is Aman")


# myname=decorator(myname)
# You can cancel writing the upper line but you need to write @decorator in just above line of the modifyer function 
myname()
