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

# # We can use the IN operator - a MEMBERSHIP OPERATOR. The IN operator isn't an exact comparison like "==". Instead, it's looking to see if that element is found in the collection it's looking in. This could be a string, a list, a tuple, etc. As long as "blue" appears somewhere in the answer, it'll be accepted

# print("Which colour is the sky? (You can type any answer that has \"blue\" in it)")
# answer = input("  >  ").lower()
# if "blue" in answer:
#     print("Correct.")

# #-------------------------------------------------------------------------

# # IF ELSE - The NOT operator

# # The NOT operator is an inverter. It flips booleans. "True" becomes "False" and the opposite. 

# print (not True) #output will be False

# shopping_list = ["orange", "apple", "banana"]
# new_item = input("Add a new item to the list: ")
# if new_item not in shopping_list: #without the not operator, a new item would evaluate to False under this code. The "not" operator flips it, so it runs
#     shopping_list.append(new_item)
# print(shopping_list)

# # The not operator is useful because it's extremely readable. It makes perfect sense to us to say "if this item is not in the shopping list, add it". It's easier to think of than trying to work out what is True and False ourselves. Let the program do that

# #-------------------------------------------------------------------------

# # FUNCTIONS - RETURN

# """
# Functions allow us to write chunks of reusable code. 

# We call the functions when we need to use them.

# Functions typically allow us to hand over dome data, and the function will process it for us. 

# """

# def add_up (num1, num2): #in this example, the function prints the result. But that limits this function. It's now only useful in cases where we want to print out the result
#     print(num1+num2)

# add_up(2,2) 

# integer_list = [1,2,3,4,5]
# def add_up_and_append(num1, num2):
#     integer_list.append(num1+num2)

# add_up_and_append(2,7)
# print(integer_list)
# #There are lots of use cases for adding two numbers together. Do we need to write a function for each possible reason? That's not very efficient. 

# # Functions typically allow us to hand over dome data. The function will process it for us - and then the function RETURNS to its caller. 
# # Part of the functions add_up job is to print num1_num2. 
# # Call the function add_up inside a print() function. What else appears when you run this?

# print(add_up(2,2)) #If we don't explicitly tell the function what information to return, it returns None
# #-------------------------------------------------------------------------

# def add_up(num1, num2):
#     return num1 + num2 #We can use the return keyword to specify what we want the function to give back to the caller

# print(add_up(4,7))

# integer_list = [1,2,3,4,5]

# integer_list.append(add_up(7,22))

# print(integer_list)

# #-------------------------------------------------------------------------

# # TUPLES

# #Same as lists. Difference is that TUPLES are not changeable and the syntax uses brackets instead of square brackets. Like lists, TUPLES are ordered and the items will have the same index position every time

# coffee_order = (
#     'Alex - Cortado', 
#     'Ben - Latte', 
#     "Charlie - Mocha"
# )

# coffee_order.append("Diane - Cappuccino") # print will say: AttributeError: 'tuple' object has no attribute 'append'

# #TUPLES have only TWO methods

# coffee_order.count("Alex - Cortado") # counts how many times the specified item appears in the collection

# coffee_order.index("Alex - Cortado") # searches the collection for the specified item and returns its index position

# # Because they can't be changed, TUPLES are a much safer kind of collection. Using a TUPLE lowers the chances of a collection getting accidentally changed

# #-------------------------------------------------------------------------

# DICTIONARIES

"""
In real life, dictionaries hold words and their definitions in pairs. 
In Python, dictionaries are collections of data. 
This data is stored in KEY:VALUE pairs
"""

capital_cities = {
    "England" : "London", 
    "Scotland" : "Edinburgh",
    "Wales" : "Cardiff",
    "Northern Ireland" : "Belfast",
    "Ireland" : "Dublin"
}

"""
Dictionaries are wrapped in {} curly brackets

Keys and pairs are split by : a colon

Elements are split by , a comma

Whereas lists let us look things up their values using a index, dictionaries let us look things up via the key.

"""

print(capital_cities["Ireland"])

""" 
Dictionaries can't contain duplicates. Newer values will overwrite old ones. Unlike tuples, dictionaries are changeable. 
"""

capital_cities = {
    "England" : "London", 
    "Scotland" : "Edinburgh",
    "Wales" : "Cardiff",
    "Northern Ireland" : "Belfast",
    "Ireland" : "Dublin",
    "Wales" : "Swansea"
}

print(capital_cities)

"""

"""
