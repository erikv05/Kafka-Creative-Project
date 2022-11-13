
class Landmark:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    
    def play_landmark(self, game):
        print("Super triggered")

class FirstEncounter(Landmark):
    def play_landmark(self, game):
        print("It's been two days and your parents become suspicious.")
        print("Your mom asks ")