# Date 19-3-2021
import random

aman1 = random.randint(0, 200)
aman2 = random.random()*100  # This is the sub module of the random module
print("Your random number is \'"+str(aman2)+"\'.")

# Now let's discuss about how to get random item from the list
list1 = ["Iron Man", "Captain America", "Black Panther",
         "Hawkeye", "Thor", "Hulk", "Black Widow", "Vision",
         "War Machine", "Spider Man", "Nova"]
print(random.choice(list1))  # choice is a attribute of random libirary

# remember no need to learn attributes or functions of any module
