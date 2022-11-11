class Landmark:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    
    def play_landmark(self):
        print("Super triggered")

class FirstEncounter(Landmark):
    def play_landmark(self):
        print("First encounter play method called")