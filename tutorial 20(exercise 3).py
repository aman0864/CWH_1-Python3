# Date 15-2-2021

# In this exercise you need to make a game of guessing numbers by using python
# In this game you will give user 6 chance to guess a number
# Make sure to do following things
# Print gusses left with the user after every guess made by the user
# After every guess of the user print that his guessed number is more or less than the number which he/she has to guess
# If user unable to guess the number print "Game Over" and ask user that he/she want to play the program again or not
# If user guessd the number then print "Congraulations!", and guesses he/she taked to guess the number

numguess = 20
# it is the number which user needs to guess

print("Press \"P\" to play the game and press \"E\" to exit the game")
choice = input()
choice = choice.upper()

guessleft = 6
while(choice == "P") and (guessleft >= 1):
    print("\nEnter a number to play a guessing number game.")
    numbyuser = int(input())
    if (numbyuser > numguess):
        guessleft = guessleft-1
        print("\n\n\nYou need to guess a smaller number\nGuess left by you is:", guessleft)
    elif (numbyuser < numguess):
        guessleft = guessleft-1
        print("\n\n\nYou need to guess a bigger number\nGuess left by you is:", guessleft)
    elif (numbyuser == numguess):
        guessleft = 6-guessleft
        print("\n\n\nCongraulations! You had guessed the number\nYou had taken",1+guessleft, "guesses to complete the game")
        guessleft = 6

if (choice == "E") or (guessleft == 0):
    print("\n\nGame Over!")
    print(5*"\n")
    print("Press \"P\" to play the game again and press \"E\" to exit the game")
    choicebyuser = input()
    choice = choicebyuser.upper()
