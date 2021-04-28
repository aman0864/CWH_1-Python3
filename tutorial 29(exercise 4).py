# Date 19-3-2021

# Take input from user in "n" i.e. number of rows
# also take in put from user in "1" and "0" i.e. in boolean operators
# and print this pattern according to the value of n(If user enter 1(i.e.True in boolean operator))
# *
# **
# ***
# ****
# *****
# print this pattern according to the value of n(If user enter 1(i.e.True in boolean operator))
# *****
# ****
# ***
# **
# *


print("Tell us that how many rows you want in your pattern:")
num1 = int(input())

print("Please, Enter \"1\" or \"0\" according to the need for your pattern:")
pattern = input()

print("Tell us what character you need to show in your pattern:")
character = input()

# print(pattern)

if (pattern == "1"):
    execution = 1
    # for true or 1 value in pattern
    # print("true1")
    while num1 >= 1:
        # stars =
        print(execution*character)
        # print("\n")
        num1 -= 1
        execution += 1

elif (pattern == "0"):
    execution = num1
    # print("false0")
    # for false or 0 value in pattern
    while num1 >= 1:
        # stars =
        print(execution*character)
        # print("\n")
        num1 -= 1
        execution -= 1

else:
    print("Please re-enter the values")
