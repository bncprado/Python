import random
from player import Player
#This is a class filled with clues that the player will encounter in the game. 
class Clue:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def search(self):
        pass

# Each of them have different sections of clues that would go in random for the player that finds himself/herself the choices that she makes. 
class Footprints(Clue):
    def __init__(self):
        super().__init__("Footprints", "Caves")

    def search(self):
        print("You found some footprints!")
        Player.inventory.append(self)

class OgreHair(Clue):
    def __init__(self):
        super().__init__("Ogre Hair", "Swamp")
#This shows that the player has found the ogre's hair near the swamp. 
    def search(self):
        print("You found strands of ogre hair!")
        Player.inventory.append(self)

#function for clues within the game
def get_random_clue():
    clues = [Footprints(), OgreHair()]
    return random.choice(clues)

