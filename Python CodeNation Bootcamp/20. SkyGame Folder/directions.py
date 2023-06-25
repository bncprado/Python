from enum import Enum
# This is a class where we use for directions as they appear in our terminal. 
# When they wrote down in the terminal as they ask which direction the player need to go will appear in that section. Such as North, South, West and East.
# There are other various places as well which are Cave, Tavern, Farm and Swamp which are connected towards the four cardinal directions.
class Directions(Enum):
    START = "start"
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"
    SWAMP = "swamp"
    CAVE = "cave"
    TAVERN = "tavern"
    FARM = "farm"
   
# This is classmethods, it shows the places that the user is currently at while playing the game. 
    @classmethod
    def choices(cls, current_location):
        """
        Returns a list of available directions based on the current location.
        """
        if current_location == cls.START:
            return [cls.NORTH, cls.SOUTH, cls.WEST, cls.EAST]
        elif current_location == cls.NORTH:
            return [cls.SOUTH, cls.EAST, cls.WEST]
        elif current_location == cls.EAST:
            return [cls.NORTH, cls.SOUTH, cls.WEST]
        elif current_location == cls.SOUTH:
            return [cls.NORTH, cls.EAST, cls.WEST]
        elif current_location == cls.WEST:
            return [cls.NORTH, cls.EAST, cls.SOUTH]
        else:
            raise [ValueError(f"Invalid location: {current_location}")]
