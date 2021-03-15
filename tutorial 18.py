# Date 15-2-2021

# In this tutorial you will learn about True, continue, and break functions of while loop


print("Enter a number:", end=" ")
num1 = int(input())

if num1 <= 100:
    while (num1 <= 100):
        while(True):
            # True function will help while loop to execute infinite times
            print("Enter another number:", end=" ")
            num1 = int(input())
            if (num1 <= 100):
                continue
                # Continue function will help while loop to terminate it's below program(Which are inside it's while loop) and execute it's program again from starting
            elif(num1 > 100):
                print("Your entered number is bigger than 100")
                # Break function will help while loop to Abot his full execute lines of program which are below while loop
                break
elif num1 >= 100:
    print("Your entered number is bigger than 100")
