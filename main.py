#TODO: add instructions to README
#TODO: add citaitons to README

import time
import webbrowser
import landmark

class Game:

    hours_to_survive = 720
    hours_survived = 0
    food = 0
    water = 0
    currency = 500
    health = ["good", "moderate", "marginal", "critical"]
    current_health = 0
    landmarks = [landmark.FirstEncounter("Test", 48)]

    def raise_health(self):
        if (self.current_health == 0):
            return
        self.current_health -= 1

    def lower_health(self):
        self.current_health += 1
        if (self.current_health >= len(self.health)):
            return True
        return False


    def get_int_input(self):
        while (True):
            try:
                enter = input("Input: ")
                return int(enter)
            except:
                print("Input could not be converted to an integer. Please try again.")

    def get_int_input(self, msg):
        while (True):
            try:
                enter = input(msg)
                return int(enter)
            except:
                print("Input could not be converted to an integer. Please try again.")

    def input_equals_str(self, compare):
        while (True):
            try:
                enter = input("Input: ")
                enter = str(enter)
                if (compare.lower() == enter.lower()):
                    return True
                return False
            except:
                print("Your input could not be converted to a string. Please try again.")

    def input_equals_str(self, compare, msg):
        while (True):
            try:
                enter = input(msg)
                enter = str(enter)
                if (compare.lower() == enter.lower()):
                    return True
                return False
            except:
                print("Your input could not be converted to a string. Please try again.")

    def instructions(self):
        if (self.input_equals_str("yes", "Do you need instructions? (YES/NO): ")):
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

    def buy_goods(self):
        print("You will need food and water. Occasionally, someone might steal your resources.")
        print("Otherwise, you will need 5 pieces of food and 1 glass of water per day.")
        print("Food costs $1/piece and water costs $3/glass.")
        food_cost = 1
        water_cost = 3
        done = False
        while (not done):
            enter = input("Please input the resource you wish to buy or ENTER to finish buying goods (FOOD/WATER/ENTER): ")
            if (enter.lower() == "food"):
                self.food = self.get_int_input("Amount of food purchased: ")
            elif (enter.lower() == "water"):
                self.water = self.get_int_input("Amount of water purchased: ")
            elif (enter == ""):
                if ((self.food * food_cost + self.water * water_cost) > self.currency):
                    print("You don't have enough money for this bill!")
                else:
                    done = True
            print("Total bill: $" + str(self.water * water_cost + self.food * food_cost))
        self.currency -= (self.water * water_cost + self.food * food_cost)

    def progress(self):
        print("You have survived " + str(self.hours_survived) + " hours.")
        enter = input("Would you like to progress time or assess the situation ([P]ROGRESS/[A]SSESS): ")
        
        if ((enter.lower() == "assess") | (enter.lower() == "a")):
            self.print_stats()
            #TODO: add sneaking out feature
            enter = input("Would you like to try and sneak out to get food or water (NO/FOOD/WATER): ")
            #if (enter.lower() == "food"):
        else:
            self.hours_survived += 24
            self.food -= 5
            self.water -= 1
            #TODO: add food stealing feature

    def print_stats(self):
            print("You have survied " + str(self.hours_survived) + " hours. You have $" + str(self.currency) + " left.")
            print("You have " + str(self.food) + " pieces of food and " + str(self.water) + " glasses of water left.")
            print("Your health is " + str(self.health[self.current_health]) + ".")
        
    def main(self):
        done = False
        dead = False
        self.instructions()
        self.buy_goods()
        while ((self.hours_survived < self.hours_to_survive) & (done == False)):
            self.progress()
            if (bool(self.landmarks)):
                if (self.hours_survived >= self.landmarks[0].distance):
                    self.hours_survived = self.landmarks[0].distance
                    self.landmarks[0].play_landmark()
                    self.landmarks.pop(0)
        if (done == False):
            print("Hours survived: 720")
            print("Congratulations! You have successfully survived life as a bug.")

        


action = Game()
action.main()