# Date 20-3-2021

import random
# import emoji

aichoice = "None"
userchoice = "None"
username = str(input("Please Enter you name to play the game:\n").capitalize())
print(username)
i = int(input("So, "+username+" how many times you need to play with a Computer:\n"))
score = [0, 0]


def aiturn():
    """
    This function will help the bot to choose his option (i.e. Snake, Water, Gun)
    """
    global aichoice
    ch = ["S", "W", "G"]
    aichoice = (random.choice(ch))
    return aichoice


def userturn():
    """
    This function will take input from user in the form of S, W, G (i.e. Snake, Water, Gun)
    """
    global userchoice
    userchoice = input(
        "Press S for Snake\nPress W for Water\nPress G for Gun\n")
    userchoice = userchoice.upper()
    if (userchoice == "S") or (userchoice == "W") or (userchoice == "G"):
        return userchoice
    else:
        print("Please enter values in S, W, G only, and restart the game.")
        global i
        i=0


while(i >= 1):
    userturn()
    aiturn()
    if (userchoice == "S") and (aichoice == "W"):
        score[0]+=1
        str1 = f"You won this turn\nScore of {username}: {score[0]}\nScore of Computer: {score[1]}\n\n"
        print(str1)
        i -= 1
    elif (userchoice == "W") and (aichoice == "G"):
        score[0]+=1
        str1 = f"You won this turn\nScore of {username}: {score[0]}\nScore of Computer: {score[1]}\n\n"
        print(str1)
        i -= 1
    elif (userchoice == "G") and (aichoice == "S"):
        score[0]+=1
        str1 = f"You won this turn\nScore of {username}: {score[0]}\nScore of Computer: {score[1]}\n\n"
        print(str1)
        i -= 1
    elif (userchoice == "S") and (aichoice == "S"):
        str1 = f"This turn is aboted because both players chosed same choice\nScore of {username}: {score[0]}\nScore of Computer: {score[1]}\n\n"
        print(str1)
    elif (userchoice == "W") and (aichoice == "W"):
        str1 = f"This turn is aboted because both players chosed same choice\nScore of {username}: {score[0]}\nScore of Computer: {score[1]}\n\n"
        print(str1)
    elif (userchoice == "G") and (aichoice == "G"):
        str1 = f"This turn is aboted because both players chosed same choice\nScore of {username}: {score[0]}\nScore of Computer: {score[1]}\n\n"
        print(str1)
    elif (userchoice == "W") and (aichoice == "S"):
        score[1]+=1
        str1 = f"You lose this turn\nScore of {username}: {score[0]}\nScore of Computer: {score[1]}\n\n"
        print(str1)
        i -= 1
    elif (userchoice == "G") and (aichoice == "W"):
        score[1]+=1
        str1 = f"You lose this turn\nScore of {username}: {score[0]}\nScore of Computer: {score[1]}\n\n"
        print(str1)
        i -= 1
    elif (userchoice == "S") and (aichoice == "G"):
        score[1]+=1
        str1 = f"You lose this turn\nScore of {username}: {score[0]}\nScore of Computer: {score[1]}\n\n"
        print(str1)
        i -= 1

if(score[1]>score[0]):
    # It means that computer won the match
    str1=f"Sorry! You lose the match by {score[1]-score[0]} points\n{username}\'s score: {score[0]}\nComputer\'s score: {score[1]}"
    print(str1)
elif(score[0]>score[1]):
    # It means that user won the match
    str1=f"Congraulations! You won the match by {score[0]-score[1]} points\n{username}\'s score: {score[0]}\nComputer\'s score: {score[1]}"
    print(str1)
elif(score[0]==score[1]):
    # It means that the match is drawen
    # print("Unfortunately! Match has considered draw")
    str1=f"Unfortunately! Match has considered draw; as both players score is same i.e. {score[0]}"
    print(str1)

str1=input("Please any key to exit the game")

# userturn()
# print(userchoice)
# print("Welcome to our Snake, Water, Gun game!")
