# Date 14-2-2021

# Write a programe which ask a user to input his/her age and tell user that he can drive or not
# for 18 less tell can't drive
# for 18 tell you need to come to us for checkup
# for 18 plus tell can drive

print("Tell us your age, So that we can tell you that you can drive or not")
age = int(input())

if age > 18:
    print("Congratulations! you can drive")
elif age < 18:
    print("Soory! you can't drive")
elif age == 18:
    print("You need to come to us for checkup")
