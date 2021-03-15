# Date 15-2-2021

tuple1 = ("Aman", "Suresh", "Mukesk", "Ramesh", "Naresh", "Nayan", "Carry")
# you can also make a list, set etc. in the place of tuple
# You can use loops such as for loops to do repeated things
# Following is a syntax of for loop
for boys in tuple1:
    print(boys)

# Let's take another example of for loop
# Now let us make a list inside a list and try to print it using for loop
list1 = [["Aman",7,897], ["Suresh",15,485], ["Mukesk",19,1098], ["Ramesh",12,568], ["Naresh",1,987], ["Nayan",8,732], ["Carry",5,453],["Aman",23,739]]
# print(type(set1))
for things,firstnumbers,secondnumber in list1:
    print("His name is",things,"and his first number is",firstnumbers,"his second number is",secondnumber) 
