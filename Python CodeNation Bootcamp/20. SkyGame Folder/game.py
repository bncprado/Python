import random
import time
from player import Player
from directions import Directions
from obstacles import Snake, PoisonousSpider, Rabbit, Birds, Farmer
from clues import Footprints, OgreHair
def typewriter(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.3)
    print()

class Game:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.player = None
        self.current_location = Directions.START
        self.game_over = False
        self.found_donkey = False
        self.lives = 3
        self.start_time = None
        self.kill = None


    def get_player_name(self):
        typewriter("\nPlease, enter your name: ")
        name = input()
        self.player = Player(name, 3)
        
    #intro    
    def start(self):
        self.get_player_name()
        self.start_time = time.time()
        typewriter(f"\nWelcome to Ogre's Quest: In Search of Donkey, {self.player.name}!\n")
        typewriter(f"You have {self.time_limit // 60} minutes to find Ogre's Donkey.\n")
        typewriter("Good luck!\n")
        while not self.game_over:
            self.print_location()
            self.get_user_input()
            if time.time() - self.start_time > self.time_limit:
                print("Time's up! Game over.\n")
            self.game_over = True
    
    def print_location(self):
        typewriter(f"Time remaining: {int(self.time_limit - (time.time() - self.start_time))} seconds.\n")
        typewriter(f"Lives remaining: {self.lives}\n")
        typewriter("Enter the direction where you want to go?\n")
        for i, direction in enumerate(Directions.choices(self.current_location), start=1):
            print(f"{i}. {direction.name}")

    def get_user_input(self):
        valid_choices = [direction.value for direction in Directions.choices(self.current_location)]
        user_input = input("\nEnter a direction: \n").lower()
        while user_input not in valid_choices:
            user_input = input("Invalid input. Enter a direction: \n").lower()
        self.current_location = Directions(user_input)
        if self.current_location == Directions.NORTH:
            self.search_swamp()
        elif self.current_location == Directions.SOUTH:
            self.search_caves()
        elif self.current_location == Directions.EAST:
            self.search_tavern()
        elif self.current_location == Directions.WEST:
            self.search_farm()
        elif self.current_location == Directions.START:
            self.restart_game() 
        else:
            self.random_event()
                    
    def search_swamp(self):
            typewriter("\nYou have reached the swamp.\n")
            typewriter("You have encountered a flesh-eating fish.\n") 
            x = input("Do you want to go into the swamp? y/n: ").capitalize()
            if x == "N":
                typewriter("You are forced to go back to the beginning")
                self.current_location = Directions.START
                self.print_location()
                self.get_user_input()
            else:
                typewriter("Too bad, you' re dead.\n")
            
            
            
    def search_caves(self):
        typewriter("\nYou have found the caves!\n")
        obstacle = random.choice([PoisonousSpider(), Farmer()])
        if isinstance(obstacle, Farmer):
            self.found_donkey = True

            typewriter("You have found an excellent clue: Ogre Hair!\n")
            typewriter("Brilliant, you've found Ogre's Donkey and won the game!\n")
            self.game_over = True
                                                                                                                                                                                                                                                                                                                                                                                                                                
        else:
            typewriter(f"You encountered a {obstacle.name}!\n")
            obstacle.is_deadly
            typewriter(f"{obstacle.name} killed you.\n")
            self.game_over = True
        

    def search_farm(self):
        typewriter("\nYou have reached the farm.\n")
        obstacle = random.choice([PoisonousSpider(), Farmer()])
        if isinstance(obstacle, Farmer):
            print("You found the Farmer!\n")
        
            if isinstance(obstacle, PoisonousSpider):
                print("You found a Spider. You dead!\n")
        else:
            typewriter("You ask the farmer where the donkey is.\n")
            typewriter("He tells you to look in the caves.\n")
            self.current_location == Directions.CAVE
            self.random_event()

    def search_tavern(self):
        typewriter("The Meadows are really nice\n") 
        typewriter("You are now at the tavern in the Kingdom. The Donkey is not here.\n") 
        x = input("Would you like to go to the caves? y/n: ").capitalize()
        if x == "Y":
            typewriter("\nYou found the birds, they have told you to look in the Caves for the donkey\n")
            typewriter("You are now going to the Caves\n")
            self.current_location == Directions.CAVE
            typewriter("Brilliant, you've found Ogre's Donkey and won the game!\n")
            self.game_over = True
            
        else:
            typewriter("You found the rabbit\n")
            typewriter("You are going to the farm\n")
            self.current_location == Directions.WEST
            self.search_farm()
            typewriter("Brilliant, you've found Ogre's Donkey and won the game!\n")
            self.game_over = True

    def restart_game(self):
            typewriter("You have restarted the game.\n")
            self.current_location = Directions.START
            self.player.clear_inventory()
            self.found_donkey = False
            self.game_over = False
            self.start_time = None

    def random_event(self):
        obstacle = random.choice([Footprints(), PoisonousSpider(), Rabbit(), Birds()])
        if isinstance(obstacle, Footprints):
            typewriter("You found some footprints.\n")
            self.search_swamp()
        elif isinstance(obstacle, Birds):
            typewriter("You found Birds.\n")
        else:
            typewriter(f"You encountered a {obstacle.name}!\n")
            if obstacle.is_deadly:
                print(f"{obstacle.name} has killed you.\n")
                self.lives -= 1 
                if self.lives == 0:
                   self.game_over = True
                else:
                   typewriter(f"You have {self.lives} lives left.\n")

    def print_game_over(self):
        if self.found_donkey:
            typewriter("Congratulations! You won the game.\n")
        else:
            typewriter("Game over.\n")
        typewriter(f"You found {len(self.player.inventory)} clues.\n")
        typewriter(f"You lasted {int(time.time() - self.start_time)} seconds.\n")
        typewriter(f"You have {self.lives} lives left.\n")

game = Game(time_limit=300)
game.start() 


# This is a Python program for an adventure game called "Ogre's Quest: In Search of Donkey".

# The program imports modules such as random, time, player, directions, obstacles, and clues.

# The "typewriter" function is used to print text on the screen, with a slight delay between each character, to create a typewriter-like effect.

# The "Game" class is the main class that contains methods for starting the game, getting user input, and searching for clues to find Ogre's Donkey.

# The "init" method initializes the game with the time limit, player, current location, game over status, number of lives, start time, and the kill.

# The "get_player_name" method prompts the user to enter their name and initializes a new player object with the given name and three lives.

# The "start" method starts the game and prints the introduction message along with the time limit and the number of lives remaining. The method then calls the "print_location" method, which displays the current location and prompts the user to enter a direction. If the time limit is exceeded, the game is over.

# The "print_location" method displays the time remaining, the number of lives remaining, and the available directions to move in.

# The "get_user_input" method gets the user's input and checks whether the input is valid. If the input is valid, it changes the current location of the player based on the input. If the location is the starting point, the game is restarted. Otherwise, it calls the "random_event" method.

# The "search_swamp" method displays a message that the player has reached the swamp and prompts the user to decide whether to enter it or not. If the user chooses not to enter, they are forced to go back to the beginning. Otherwise, they die.

# The "search_caves" method displays a message that the player has reached the caves and randomly selects an obstacle for the player to encounter. If the player encounters a farmer, they have found Ogre's Donkey and won the game. Otherwise, the player is dead.

# The "search_farm" method displays a message that the player has reached the farm and randomly selects an obstacle for the player to encounter. If the player encounters a farmer, they are told to look for Ogre's Donkey in the caves. Otherwise, the player asks the farmer for help.

# The "search_tavern" method displays a message that the player has reached the tavern and prompts the user to decide whether to go to the caves or the farm. If the user chooses the caves, they are told to look for Ogre's Donkey there. If the user chooses the farm, they encounter a rabbit, and the game proceeds as in the "search_farm" method.

# The "restart_game" method restarts the game by changing the current location to the starting point.