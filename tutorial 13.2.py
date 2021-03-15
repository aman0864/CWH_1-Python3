# Date 14-2-2021

# In this tutorial we will learn that how to know that the variable is inside it or not in data types (Such as Lists, Sets, Tuple, Ditionary)

# Let's create a list
list1 = [56, 89, 74, 1, 0, 23, 6, 5, 147, 435, 489]
print("Write a number to check it is in our list or not")
inum = int(input())
if inum in list1:
    print("Yes!", inum, "is there in the list")
if inum not in list1:
    print("No!", inum, "is not there in the list")
