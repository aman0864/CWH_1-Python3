# Date 20-3-2021

# In this tutorial we will learn about time module which is used to know the time take by the program to finish

import time
import math

i = 0
initialtime1 = time.time()
while(i < 45):
    i += 1
    print("Factorial of", i, "is", math.factorial(i))
timebywhile = time.time()-initialtime1
print("\n\nTime taken by while loop is:", timebywhile, "\n\n\n")

print(10*"\n")
i = 0
initialtime2 = time.time()

for num1 in range(45):
    i += 1
    print("Factorial of", i, "is", math.factorial(i))
timebyfor = time.time()-initialtime2
print("\n\nTime taken by for loop is:", timebyfor, "\n\n\n")

# The upper syntax will help you to know the time taken by for loop and while loop to execute


# Now let's discuss about how to stop working of our program for some time
print("Now \'Aman is a good boy\' will print 45 time with the gap of 2 seconds after every line")
i = 0
while(i < 45):
    print("Aman is a good boy")
    time.sleep(2)  # this line is the reson for printing evey line after 2 seconds
    i += 1
