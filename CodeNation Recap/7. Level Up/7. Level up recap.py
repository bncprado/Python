# """
# Now we've got a solid understanding of the coding fundamentals, let's level up some of our knowledge

# If/Else
#   } Truthy and Falsy
#   } Not and In

# Functions
#   } Return

# Lists
#   } Tuples
#   } Dictionaries

# Error Handling
#   } Try/Except

# Loops
#   } While True
#   } Break

# """

# # IF/ELSE - Truthy and Falsy

# # We know we can compare two values, and that they'll be evaluated to True or False

# music = "classical"
# print(music == "classical") #It'll return true

# # But values also have their own inherent Boolean values without needing to be evaluated as part of a bigger expression

# music = "classical" # Truthy
# shopping_list = []  # Falsy
# num = 0             # Falsy
# name = ""           # Falsy
# my_name = "Dave"    # Truthy

# """
# FALSY VALUES:
# - Empty strings "" 
# - Interget 0
# - Float 0.0
# - Any other mathematical 0
# - Empty collections
# - None
# - False

# EVERYTHING ELSE IS TRUTHY
# """

# #-------------------------------------------------------------------------

# #This code won't wrok as expected. It's looking to see if the value of "name" is the same as the boolean "True", which it won't be. One is a string and other is a boolean

# print("What's your name?")
# name = input (" > ")
# if name == True: # We're not looking to see if name is equal to True. We want to see if name is a truthy value. Is it something other than an empty string? 
#     print(f"Hello {name}, how are you")
# else:
#     print ("You did not give you your name!")


# print("What's your name again?")
# name = input (" > ")
# if name: #This if statement is just looking to see if name is truthy, which it will be for anything other than the user hitting enter (which would be an empty string)
#     print(f"Hello {name}, how are you")
# else:
#     print ("You did not give you your name!")

# #-------------------------------------------------------------------------

# IF ELSE - The IN operator





