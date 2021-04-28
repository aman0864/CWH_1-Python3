# Date 20-3-2021

# In this tutorial we will learn about map and filter functions

# Suppose we are having a list of numbers and we want that list to typecast in a list with integer values only
# Well in that case we will use map function
list1 = ["78", "1", "351", "646", "4", "33",
    "43", "3324", "354", "65", "423", "2"]

# it will just change the string variables into integer variables
list1 = list(map(int, list1))
print(list1[11]+2)

# now let's discuss about filter function
# Filter function just simpily return only those values which are true
def greater_value(items):
    return items > 10


print(list(filter(greater_value, list1)))
