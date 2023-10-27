import random
# These are obstacles and they are in a class for the game. 
# They are different obstacles but they are random along with it. 
class Obstacle:
    def __init__(self, name, is_deadly=False):
        self.name = name
        self.is_deadly = is_deadly

    def encounter(self, player):
        pass

class Snake(Obstacle):
    def __init__(self):
        super().__init__("Snake", is_deadly=True)

    def encounter(self, player):
        print("You have encountered a snake!")
        print("It bites you and you lose a life.")
        player.lives -= 1

class PoisonousSpider(Obstacle):
    def __init__(self):
        super().__init__("Poisonous Spider", is_deadly=True)

    def encounter(self, player):
        print("You have encountered a poisonous spider!")
        print("It bites you and you lose two lives.")
        player.lives -= 2

class Horse(Obstacle):
    def __init__(self):
        super().__init__("horse", is_deadly=False)

    def encounter(self, player):
        print("You have encountered a horse!")
        print("It offers to carry you to the next location.")
        player.current_location += 1

class Farmer(Obstacle):
    def __init__(self):
        super().__init__("farmer")

    def encounter(self, player):
        print("Watch out for the Farm er, He's not genuine!")
        print("He tells you to go to the Swamp.")
        player.current_location -= 1

class Rabbit(Obstacle):
    def __init__(self):
        super().__init__("rabbit")

    def encounter(self, player):
        print("You have encountered a rabbit!")
        print("It hops away and leaves you alone.")

class Birds(Obstacle):
    def __init__(self):
        super().__init__("birds")

    def encounter(self, player):
        print("You have encountered some birds!")
        print("They fly away and leave you alone.")

class ObstacleGenerator:
    @staticmethod
    def generate_obstacle():
        obstacle_classes = [Snake, PoisonousSpider, Farmer,  Rabbit, Birds]
        obstacle_class = random.choice(obstacle_classes)
        return obstacle_class()
