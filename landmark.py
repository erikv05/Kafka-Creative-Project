import webbrowser
class Landmark:
    def __init__(self):
        self.distance = 0
    def play_landmark(self):
        print("Super play triggered")
        return 0

class FirstEncounter(Landmark):
    def __init__(self):
        self.distance = 96
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
        self.distance = 192
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
            return -1
            #TODO: add video

class FoodDecision(Landmark):
    def __init__(self):
        self.distance = 288
    def play_landmark(self):
        print("Your sister is concerned and wants to give you food.")
        print("She puts some fresh food and some rotten food on your plate. Which do you eat?")
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