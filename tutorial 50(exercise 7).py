# Date 20-3-2021

# Healthy programmer
# Write a program in which you need to remind a programmer for the following things
# and you need to play an audio to as remainder
# to drink 250 ml of water in every 40 minutes
# eyes exercise in every 30 minutes
# physicial exercise in every 50 minutes
# Also save that person' whole data in form of a .txt file
# Note: Use pygame module for playing tunes

import pygame
import time


def eye():
    time.sleep(1800/300)
    val1 = "none"
    # on music
    val1 = input(
        "Your time is for Eye Exercise\nType Done to close the programe:\n").capitalize()
    if (val1 == "Done"):
        # Stop music 
    else:
        eye()
    timeforeye = time.time()
    # print(num1)


def wtr():
    time.sleep(2400-tt1)


# print("\N{kissing face}")
eye()
