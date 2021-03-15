# Date 14-2-2021

# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9=77, 56/6 = 4
# Your program should take operator and the two numbers as input from the user

print("First enter the operator of the question")
operator = input()
print("Now enter the first value of the question")
num1 = int(input())
print("Now enter the second value of the question")
num2 = int(input())

if operator == "*" and num1 == 45 and num2 == 3:
    print("Answer is 555")
elif operator == "+" and num1 == 56 and num2 == 9:
    print("Answer is 77")
elif operator == "/" and num1 == 56 and num2 == 6:
    print("Answer is 4")
elif operator == "/":
    print("Answer is", num1 / num2)
elif operator == "-":
    print("Answer is", num1 - num2)
elif operator == "+":
    print("Answer is", num1 + num2)
elif operator == "*":
    print("Answer is", num1 * num2)
else:
    print("Enter a valid operator")