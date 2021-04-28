# Date 18-3-2021

# In this tutorial we will learn about-
# Try Except Exception Handling In Python  

try:
    print("Enter the value of A")
    a = int(input())
    print("Enter the value of B")
    b = int(input())
    print("Sum of your entered numbers is ",a+b)
except Exception as e:
    print("An Error occured, and that error is\n",e)    

print("\nThanks, to use our code!\n")