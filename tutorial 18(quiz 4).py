# Date 15-2-2021

# Write a programe which will take continues input from the user till the user does not enter the value greater than 100

print("Enter a number:", end=" ")
num1 = int(input())


while (num1 <= 100):
    while(True):
        print("Soory! Your entered number i.e.",num1,"is smaller than 100")
        num1 = int(input())
        if (num1 <= 100):
            continue
        elif(num1>100):
            print("Congratulations! Your entered number i.e.",num1,"is bigger than 100")
            break
