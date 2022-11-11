#TODO: add instructions to README
#TODO: add citaitons to README

import time
import webbrowser
from landmark import Landmark

hours_to_survive = 720
food = 0
currency = 500

def getIntInput():
    while (True):
        try:
            enter = input("Input: ")
            return int(enter)
        except:
            print("Input could not be converted to an integer. Please try again.")

def getIntInput(msg):
    while (True):
        try:
            enter = input(msg)
            return int(enter)
        except:
            print("Input could not be converted to an integer. Please try again.")

def inputEqualsStr(compare):
    while (True):
        try:
            enter = input("Input: ")
            enter = str(enter)
            if (compare.lower() == enter.lower()):
                return True
            return False
        except:
            print("Your input could not be converted to a string. Please try again.")

def inputEqualsStr(compare, msg):
    while (True):
        try:
            enter = input(msg)
            enter = str(enter)
            if (compare.lower() == enter.lower()):
                return True
            return False
        except:
            print("Your input could not be converted to a string. Please try again.")

def instructions():
    if (inputEqualsStr("yes", "Do you need instructions? (YES/NO): ")):
        print()
        print("THIS PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM")
        print("Whoops... I think that's the wrong program. Anyways...")
        print("One day you wake up and you turn into a massive bug. You still")
        print("have some of your voice, but not for long. Your goal is to survive")
        print("one month as a bug in the same house as your hostile family. After")
        print("one month, you will be granted your freedom, but it wont be easy.")
        print()
        print("Any time you are asked to input yes/no, the program will default to no")
        print("if you input something like, \'I BET YOU DIDN\'T CONSIDER THIS CASE ERIK")
        print("MWAHAHHAHAHA\'.")
        print()
        print("This game works mechanically like the Oregon Trail game from the \'80s.")
        print("Instead of making distance over the trail, you make time in your room.")
        print("You will have resources that you need to save, along with about")
        print("20 major events taken from the novel that you will have to survive. Use")
        print("your resources wisely, as you never know when they will come in handy!")
        print()
        print("-")
        time.sleep(0.1)
        print("-")
        time.sleep(0.1)
        print("-")
        time.sleep(0.1)
        print()
        print("Good luck!")

def buy_goods():
    print("")

def main():
    instructions()


try:
    main()
except:
    print("Unknown exception occured")