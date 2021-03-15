# Date 15-2-2021

# Make a and print only numbers which are greater than or equal to 6
# Note: That list must contain anything i.e. name, numbers etc.

list1 = list(["Aman", "45", "20", "Rohit", "+", "2",
              "Sumit", "98", "4", "6", "0", "8", "*", "Rohan"])
for items in list1:
    if str(items).isnumeric() and int(items) >= 6:
        print(items)
