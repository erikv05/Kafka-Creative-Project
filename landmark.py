import webbrowser
import time
from threading import Thread
import random
class Landmark:
    def __init__(self):
        self.distance = 0
    def play_landmark(self):
        print("Super play triggered")
        return 0

class FirstEncounter(Landmark):
    def __init__(self):
        self.distance = 90
    def play_landmark(self):
        print("It's been two days and your parents become suspicious.")
        print("Your mom sits outside your room and asks if you're okay.")
        print("Becoming increasingly worried, you hear the door creak open.")
        print("You can either jump out the window or stay and hope your parents don't kill you.")
        enter = input("Do you jump out or stay inside? (JUMP/STAY): ")
        if (enter.lower() == "jump"):
            print("SPLAT. You hit the ground and die.")
            print("Did you really think it'd be that easy?")
            return None
            #TODO: add video
        else:
            print("Your mom enters your room and finds that you've turned into a massive bug.")
            print("She screams and shuts the door.")
            return 0
            #TODO: add video

class OfficeManager(Landmark):
    def __init__(self):
        self.distance = 180
    def play_landmark(self):
        print("Your office manager has shown up, angry that you're missing work.")
        print("He asks you to come out of the room or risk losing your job.")
        print("You can either come out and try to explain the situation or just wait and hope he goes away.")
        enter = input("Do you stay inside or try to explain the situation? (STAY/GO): ")
        if (enter.lower() == "stay"):
            print("Your boss yells at you and is upset. You lose your job.")    
            return 0
            #TODO: add video
        else:
            print("You run outside and try to explain the situation. You forget that you can't talk.")
            print("Your boss runs away and your dad chases back inside with a newspaper, hitting you.")
            return 1
            #TODO: add video

class FoodDecision(Landmark):
    def __init__(self):
        self.distance = 270
    def play_landmark(self):
        print("Your sister is concerned and wants to give you food.")
        enter = input("She puts some fresh food and some rotten food on your plate. Which do you eat? (FRESH/ROTTEN): ")
        
        if enter.lower() == "rotten":
            print("Your sister assumes you like rotten food, which is correct.")
            print("She brings you some more food, gaining you 30 pieces.")
            return "food+"
            #TODO: add video
        else:
            print("Your sister assumes you like fresh food, so she takes the rotten food away and gives you fresh food instead.") 
            print("You lose 50 pieces of food.")   
            return "food-"
            #TODO: add video

class HideFromSister(Landmark):
    def __init__(self):
        self.distance = 360
    def play_landmark(self):
        print("Your sister is about to come into the room. You must hide. You have two seconds for the next prompt.")
        time.sleep(3)
        self.answer = None
        def check():
            time.sleep(3)
            if (self.answer == None) or (self.answer.lower() != "hide"):
                print("Your sister sees yor ugly face. She accidentally punches you out of fear.")
                #TODO: add video 
            else:
                print("You hide from your sister successfully.")
                self.answer = "safe"
                #TODO: add video

        Thread(target = check).start()
        self.answer = input("Enter \'HIDE\': ")
        time.sleep(3)
        if (self.answer == "safe"):
            return 0
        else:
            return 1

class AppleEncounter(Landmark):
    def __init__(self):
        self.distance = 450
    def play_landmark(self):
        print("You are hanging upside down in your room as this is your new hobby.")
        print("Your mom and Grete walk in. You can either hang on the ceiling and hope they don't see you or ")
        print("drop down and appear more disarming, but risk getting hurt.")
        enter = input("Which do you choose? (DROP/STAY): ")
        if enter.lower() == "stay":
            prob = random.random()
            if (prob < 0.1):
                print("You have successfully hidden from your mother, avoiding your dad's wrath altogether")
                return 0
            else:
                print("Your mother sees you as you hang and freaks out, fainting.")
                print("She knocks over 10 glasses of water.")
                return "water--"
        else:
            print("You drop down and your mom faints, making your dad rush in the room.")
            print("He is upset with you for hurting your mother. You can either try to explain ")
            enter = input("yourself or sit in your bed and hope he doesn't get mad. (SIT/TALK): ")
            if(enter.lower() == "talk"):
                print("You stand up and begin talking to your dad. He assumes you try to attack him.")
                print("He throws an apple and it lodges in your back.")
                #TODO: add video
                return -1
            else:
                print("You sit in your bed. Your dad is infuriated, ")
                print("taking 3 glasses of water from your room to punish you.")
                return "water-"

class Boarders(Landmark):
    def __init__(self):
        self.distance = 540
    def play_landmark(self):
        print("You hear your family meet with the boarders, as Grete plays the violin.")
        print("You can try to walk out and listen, and the violin might heal you.")
        print("Or your dad might also throw you out of the window.")
        print("You can also use the rest of your currency to bribe them for your freedom.")
        print("The more money you have left, the more likely they are to take the bribe.")
        enter = input("Which do you choose? (STAY/LISTEN/BRIBE): ")
        if enter.lower() == "bribe":
            return "bribe"
        elif enter.lower() == "listen":
            prob = random.random()
            if (prob < 0.7):
                print("You successfully listen to Grete's violin playing without getting hurt.")
                return -1
            else:
                print("Your dad is upset you would show your face as the boarders all run away.")
                print("He is fed up with your antics and throws you out the window.")
                #TODO: add video
                return None
        else:
            print("You stay in your room, sad that you don't hear Grete's violin.")
            print("The boarders leave.")
            return 0

class DadTrap(Landmark):
    def __init__(self):
        self.distance = 630
    def play_landmark(self):
        print("Your dad feels bad for everything he did.")
        print("He tells you that since you've survived for this long, you deserve your freedom.")
        enter = input("Do you trust your dad? (YES/NO)")
        if enter.lower() == "yes":
            print("He was just trying to lure you out.")
            print("He yeets you out the window.")
            #TODO: add video
            return None
        else:
            print("Your family assumes you're dead since you're not answering.")
            print("They schedule the made to take out your corpse in 2 days.")
            return 0

class Maid(Landmark):
    def __init__(self):
        self.distance = 720
    def play_landmark(self):
        print("The maid asks you if you are okay. She offers to set you free.")
        enter = input("Do you trust the maid? (YES/NO)")
        if enter.lower() == "yes":
            print("The maid helps you out of the house and escorts you to freedom.")
            #TODO: add video
            return 0
        else:
            print("The maid assumes you have died already since you do not answer.")
            print("She sprays your room with febreze, which kills you.")
            #TODO: add video
            return None