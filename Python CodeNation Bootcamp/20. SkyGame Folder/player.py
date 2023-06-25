class Player:
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def clear_inventory(self):
        self.inventory = []

# we have created a class called 'Player' with three attributes: 'name', 'lives', and 'inventory'.
# we used the '__init__' method and the  __init__ method takes two argument: 'name' aand 'lives'
# the '__init__ method also initializes the 'inventory' attribute to an empty list.
# we also used 'def' to define three seperate functions
#test comment
#new test comment