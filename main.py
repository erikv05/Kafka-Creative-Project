#TODO: add citaitons to README

import random
import time
import webbrowser
import landmark



class Game:

    def __init__(self):
        self.vids = True
        self.played_grete = False
        self.hours_to_survive = 720
        self.hours_survived = 0
        self.food = 0
        self.water = 0
        self.currency = 500
        self.health = ["good", "moderate", "marginal", "critical"]
        self.current_health = 0
        self.landmarks = [landmark.FirstEncounter(), landmark.OfficeManager(), landmark.FoodDecision(), landmark.HideFromSister(), landmark.AppleEncounter(), landmark.Boarders(), landmark.DadTrap(), landmark.Maid()]
        self.dead = False
        self.videoDict = {"thirst" : "https://youtu.be/8TmwEUHKRo8",
         "starved" : "https://www.youtube.com/watch?v=yKG0uEV54Sk",
         "bribe_failure" : "https://www.youtube.com/watch?v=1jQrROhz0d8",
         "bribe_success" : "https://www.youtube.com/watch?v=NnFxpSS4Hvo",
         "caught" : "https://youtu.be/uD7Ef8aVfVg",
         "credits" : "https://www.youtube.com/watch?v=9qcSuGpebIE",
         "grete_steal" : "https://youtu.be/Q3p8oGveOqE"}

    def play(self, event):
        if (self.vids):
            webbrowser.open_new_tab(self.videoDict[event])
    
    def raise_health(self):
        if (self.current_health == 0):
            return
        self.current_health -= 1
        print("Your health is now " + self.health[self.current_health] + ".")

    def lower_health(self):
        self.current_health += 1
        if (self.current_health >= len(self.health)):
            self.dead = True
            print("Your health has run out. You are now dead.")
            return
        print("Your health is now " + self.health[self.current_health] + ".")


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
        if (self.input_equals_str("y", "Do you need instructions? (Y/N): ")):
            print()
            print("THIS PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM")
            print("Whoops... I think that's the wrong program. Anyways...")
            print("One day you wake up and you turn into a massive bug. You still")
            print("have some of your voice, but not for long. Your goal is to survive")
            print("one month as a bug in the same house as your hostile family. After")
            print("one month, you will be granted your freedom, but it won't be easy.")
            print()
            print("Any time you are asked to input yes/no (Y/N), the program will default to no")
            print("if you input something like, \'I BET YOU DIDN\'T CONSIDER THIS CASE ERIK")
            print("MWAHAHHAHAHA\'.")
            print("Usually, you can use ENTER to cancel an action, even if not stated.")
            print()
            print("This game works mechanically like the Oregon Trail game from the \'80s.")
            print("Instead of making distance over the trail, you make time in your room.")
            print("You will have resources that you need to save, along with about")
            print("20 major events taken from the novel that you will have to survive. Use")
            print("your resources wisely, as you never know when they will come in handy!")
            print()
            print("If you drop below critical health or run out of food/water, you die.")
            print()
            print("-")
            time.sleep(0.5)
            print("-")
            time.sleep(0.5)
            print("-")
            time.sleep(0.5)
            print()
            print("Good luck!")

    def buy_goods(self):
        print("You must survive one month. You have $500.")
        print("You will need food and water. Occasionally, Grete might steal your resources.")
        print("Otherwise, you will need about 6 pieces of food and about 2 glasses of water per day.")
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
                elif (self.food < 0) | (self.water < 0):
                    print("How are you supposed to have negative food or water?")
                else:
                    done = True
            print("Total bill: $" + str(self.water * water_cost + self.food * food_cost))
        self.currency -= (self.water * water_cost + self.food * food_cost)

    def steal_food(self):
        risk = 0
        while (True):
            enter = input("How much risk do you want to take?\nThe more risk, the more food, but the more likely you get caught (LOW/MEDIUM/HIGH): ")
            if enter == "":
                return
            if (enter.lower() == "low"):
                enter = input("You have selected LOW risk. Is this correct? (Y/N): ")
                if (enter.lower() == "y"):
                    risk = 0
                    break
            elif (enter.lower() == "medium"):
                enter = input("You have selected MEDIUM risk. Is this correct? (Y/N): ")
                if (enter.lower() == "y"):
                    risk = 1
                    break
            elif (enter.lower() == "high"):
                enter = input("You have selected HIGH risk. Is this correct? (Y/N): ")
                if (enter.lower() == "y"):
                    risk = 2
                    break
            else:
                print("Invalid input. Try again.")
        prob = random.random()
        if (prob < (risk + 2) / 10):
            print("You were caught stealing food.")
            self.play_caught_hurt()
            self.lower_health()   
        if (not self.dead):
            print("You stole " + str(10 * risk + 10) + " pieces of food.")
            self.food += 10 * risk + 10
            print("You now have " + str(self.food) + " pieces of food.")

    def steal_water(self):
        risk = 0
        while (True):
            enter = input("How much risk do you want to take?\nThe more risk, the more water, but the more likely you get caught (LOW/MEDIUM/HIGH): ")
            if enter == "":
                return
            if (enter.lower() == "low"):
                enter = input("You have selected LOW risk. Is this correct? (Y/N): ")
                if (enter.lower() == "y"):
                    risk = 0
                    break
            elif (enter.lower() == "medium"):
                enter = input("You have selected MEDIUM risk. Is this correct? (Y/N): ")
                if (enter.lower() == "y"):
                    risk = 1
                    break
            elif (enter.lower() == "high"):
                enter = input("You have selected HIGH risk. Is this correct? (Y/N): ")
                if (enter.lower() == "y"):
                    risk = 2
                    break
            else:
                print("Invalid input. Try again.")
        prob = random.random()
        if (prob < (risk + 2) / 10):
            print("You were caught stealing water.")
            self.play_caught_hurt()
            self.lower_health()   
        if (not self.dead):
            print("You stole " + str(1 * risk + 2) + " glasses of water.")
            self.water += 1 * risk + 2
            print("You now have " + str(self.water) + " glasses of water.")
            
    def print_stats(self):
            print("You have survied " + str(self.hours_survived) + " hours. You have $" + str(self.currency) + " left.")
            print("You have " + str(self.food) + " pieces of food and " + str(self.water) + " glasses of water left.")
            print("Your health is " + str(self.health[self.current_health]) + ".")
    
    def play_thirst(self):
        self.play("thirst")
        print("You ran out of water and died.")
    
    def play_starved(self):
        self.play("starved")
        print("You ran out of food and died.")

    def play_caught_hurt(self):
        self.play("caught")
        print("You were caught stealing water. Your dad hits you.")

    def check_alive(self):
        if self.current_health > len(self.health):
            self.dead = True
        if self.water < 0:
            self.dead = True
            self.play_thirst()
        if self.food < 0:
            self.dead = True
            self.play_starved()

    def progress(self):
        print("You have survived " + str(self.hours_survived) + " hours total.")
        enter = input("Would you like to progress time or assess the situation ([P]ROGRESS/[A]SSESS): ")
        
        if ((enter.lower() == "assess") | (enter.lower() == "a")):
            self.print_stats()
            enter = input("Would you like to try and sneak out to get food or water (ENTER/FOOD/WATER): ")
            if (enter.lower() == "food"):
                self.steal_food()
            elif (enter.lower() == "water"):
                self.steal_water()
        else:
            self.hours_survived += 24
            self.food -= random.randrange(2, 10)
            self.water -= random.randrange(1, 3)
            self.check_alive()
            steal_prob = random.random()
            if (steal_prob < 0.2):
                stolen_food = random.randrange(0, 10)
                stolen_water = random.randrange(0, 3)
                self.food -= stolen_food
                self.water -= stolen_water
                if (not self.played_grete):
                    self.play("grete_steal")
                    self.played_grete = True
                print("Grete snuck in during the night and stole " + str(stolen_food) + " pieces of food and " + str(stolen_water) + " pieces of water.")
    
    def vid_prompt(self):
        print("There are videos that act out what is happening in the game.")
        enter = input("Would you like the videos to play during this run of the program? (Y/N): ")
        if (enter.lower() == "n"):
            self.vids = False

    
    def main(self):
        self.instructions()
        self.vid_prompt()
        self.buy_goods()
        while ((self.hours_survived < self.hours_to_survive) & (not self.dead)):
            if(not self.dead):
                self.progress()
                if (bool(self.landmarks)):
                    if (self.hours_survived >= self.landmarks[0].distance):
                        self.hours_survived = self.landmarks[0].distance
                        result = self.landmarks[0].play_landmark()
                        if (result == None):
                            self.dead = True
                        elif result == "food+":
                            self.food += 30
                        elif result == "food-":
                            self.food -= 50
                        elif result == "water-":
                            self.water -= 3
                        elif result == "water--":
                            self.water -= 10
                        elif result == -1:
                            self.raise_health()
                        elif result == 0:
                            pass
                        elif result == 1:
                            self.lower_health()
                        elif result == "bribe":
                            prob = random.randrange(0, 260)
                            if self.currency > prob:
                                print("The boarders accept your bribe. You are free.")
                                self.play("bribe_failure")
                                break
                            else:
                                print("The boarders do not accept your bribe, hurting you in the process.")
                                self.play("bribe_success")
                                self.lower_health()
                        self.landmarks.pop(0)
        if (not self.dead):
            print("Congratulations. You have beat the game. Thank you for playing!")
            self.play("credits")
            return True
        return False

while True:
    intent = Game()
    result = intent.main()
    if (result):
        break
    else:
        enter = input("You failed to beat the game. Try again? (Y/N): ")
        if (enter.lower() == "y"):
            pass
        else:
            break