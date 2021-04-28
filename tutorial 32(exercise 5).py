# Date 19-3-2021

# retrieve means to see the previous values
# lock means to enter new values without removing previous values


# In this question you need to make a Health Management System
# for three people
# for their exercise and food they eat
# First that ask user that for whom they want to set values,
# Means for Rohit, Rohan, Roni
# Now ask user that what they want to do i.e. enter/retrieve;
# After that ask user that what they want to enter exercise/food; or retrieve exercise/food;
# Now if the user choose enter; and after entering his/her values print sucessfully recorded your values
# Now if the user choose retrieve; print "Thanks for using our program"

def gettime():
    """This function will help you to get date and time"""
    import datetime
    return datetime.datetime.now()


print("\nWelocome! to our Health Management Program")
print("Now tell us that you want to edit/see whose Data")
print("1 for Rohit")
print("2 for Rohan")
print("3 for Roni")
try:
    person = int(input())
except:
    print("Please enter only integer values i.e. \"1\", \"2\", or \"3\".")

print("Now tell us what you want to do with Date")
print("1 for Adding new Data")
print("2 viewing old Data")
try:
    # dh reffers to Data Handeling
    dh = int(input())
except:
    print("Please enter only integer values i.e. \"1\", or \"2\".")

print("Now tell us what you want Exercise/Food")
print("1 for Exercise")
print("2 for Food")
try:
    # tod reffers to Type of data
    tod = int(input())
except:
    print("Please enter only integer values i.e. \"1\", or \"2\".")



if (person == 1):
    # If person is Rohit
    if (dh == 1):
        if (tod == 1):
            with open("tutorial 32.rohit.exercise.txt", "a") as file1:
                gettime()
                lock = str(input("Enter your Data:\n"))
                file1.write("["+str(gettime())+"]: "+lock+"\n")
                print("Successfully Recorded")
        elif (tod == 2):
            with open("tutorial 32.rohit.food.txt", "a") as file1:
                gettime()
                lock = str(input("Enter your Data:\n"))
                file1.write("["+str(gettime())+"]: "+lock+"\n")
                print("Successfully Recorded")
    elif (dh == 2):
        if (tod == 1):
            with open("tutorial 32.rohit.exercise.txt", "r") as file1:
                print(file1.read())
                print("Thanks for using our program.\n\n")
        elif (tod == 2):
            with open("tutorial 32.rohit.food.txt", "r") as file1:
                print(file1.read())
                print("Thanks for using our program.\n\n")

elif (person == 2):
    # If person is Rohan
    if (dh == 1):
        if (tod == 1):
            with open("tutorial 32.rohan.exercise.txt", "a") as file1:
                gettime()
                lock = str(input("Enter your Data:\n"))
                file1.write("["+str(gettime())+"]: "+lock+"\n")
                print("Successfully Recorded")
        elif (tod == 2):
            with open("tutorial 32.rohan.food.txt", "a") as file1:
                gettime()
                lock = str(input("Enter your Data:\n"))
                file1.write("["+str(gettime())+"]: "+lock+"\n")
                print("Successfully Recorded")
    elif (dh == 2):
        if (tod == 1):
            with open("tutorial 32.rohan.exercise.txt", "r") as file1:
                print(file1.read())
                print("Thanks for using our program.\n\n")
        elif (tod == 2):
            with open("tutorial 32.rohan.food.txt", "r") as file1:
                print(file1.read())
                print("Thanks for using our program.\n\n")

elif (person == 3):
    # If person is Roni
    if (dh == 1):
        if (tod == 1):
            with open("tutorial 32.roni.exercise.txt", "a") as file1:
                gettime()
                lock = str(input("Enter your Data:\n"))
                file1.write("["+str(gettime())+"]: "+lock+"\n")
                print("Successfully Recorded")
        elif (tod == 2):
            with open("tutorial 32.roni.food.txt", "a") as file1:
                gettime()
                lock = str(input("Enter your Data:\n"))
                file1.write("["+str(gettime())+"]: "+lock+"\n")
                print("Successfully Recorded")
    elif (dh == 2):
        if (tod == 1):
            with open("tutorial 32.roni.exercise.txt", "r") as file1:
                print(file1.read())
                print("Thanks for using our program.\n\n")
        elif (tod == 2):
            with open("tutorial 32.roni.food.txt", "r") as file1:
                print(file1.read())
                print("Thanks for using our program.\n\n")

else:
    print("Please re-enter your values")