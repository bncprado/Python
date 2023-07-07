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

# # IF ELSE - The IN operator

# print("Which colour is the sky?")
# answer = input("  >  ").lower()
# if answer == "blue" or answer == "the sky is blue" or answer == "sky is blue": # we could use the OR operator to accept all these answers, but that's very wordy
#     print("Correct.")

# # We can use the IN operator - a MEMBERSHIP OPERATOR. The IN operator isn't an exact comparison like "==". Instead, it's looking to see if that element is found in the collection it's looking in. This could be a string, a lista, a tuple, etc. As long as "blue" appears somewhere in the answer, it'll be accepted

# print("Which colour is the sky? (You can type any answer that has \"blue\" in it)")
# answer = input("  >  ").lower()
# if "blue" in answer:
#     print("Correct.")

# #-------------------------------------------------------------------------

# IF ELSE - The NOT operator

# The NOT operatir is an inverter. It flips booleans. "True" becomes "False" and the opposite. 

print (not True) #output will be False

shopping_list = ["orange", "apple", "banana"]
new_item = input("Add a new item to the list: ")
if new_item not in shopping_list: #without the not operator, a new item would evaluate to False under this code. The "not" operator flips it, so it runs
    shopping_list.append(new_item)
print(shopping_list)

# The not operator is useful because it's extremely readable. It makes perfect sense to us to say "if this item is not in the shopping list, add it". It's easier to think of than trying to work out what is True and False ourselves. Let the program do that

#-------------------------------------------------------------------------

# FUNCTIONS - RETURN
