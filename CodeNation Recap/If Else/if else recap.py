# music = 'classical'

# if music == 'classical':
#     print("Oh no! It's classical again")
# elif music == 'no music':
#     print("Ah, peace an quiet")
# else:
#     print ("Turn it up")

# """
# "=" is an assignment operator. It says the variable "music" is the string “classical”.

# "==" is a comparison operator. It compares the value of our music variable to the string “classical”.

# The program evaluates this comparison to a Boolean. Is it True or False?

# As soon as something is evaluated to True, the matching block of code will run, and the if statement is complete!

# """

# """
# COMPARISON OPERATORS:

# ==    Equal to 
# !=    Not equal to 
# <     Less than 
# <=    Less than or equal to 
# >     More than 
# >=    More than or equal to

# """

# #------------------------------------------------------------------------

# music = "classical"

# if music != "britpop":
#     print("I want to listen to britpop")
# else:
#     print('I love britpop!')

# """
# You might encounter "!=", that means "not equal".
# Our first condition here is, if music does not equal “britpop”

# """

# # #------------------------------------------------------------------------

# music = "Oasis"

# if music != "britpop":
#     print("I want to listen to britpop")
# elif music == "Oasis":
#     print("Turn it up!")
# else:
#     print("I live britpop!")

# """
# Even though the elif statement "Oasis" matches with the value of the variable "music", the first condition the code above will run is != (not equal) to the string "britpop".

# An if statement runs the first thing it evaluates to be True even if there is something even more True later! Be aware of the structure of your statement.

# """

# #-----------------------------------------------------------------------------

# # Which one will run?
# temperature = 80

# if temperature > 99:
#   print ("It's boiling")
# elif temperature > 90:
#   print("It's too hot")
# elif temperature > 70:
#   print("It's warm") #this one is the one that will be executed
# elif temperature > 40:
#   print("It's just right")
# else:
#   print("it's a bit chilly")

# #-----------------------------------------------------------------------------

# """
# LOGICAL OPERATORS

# Logical operators are symbols or words that connect two or more expressions. They evaluate both conditions on either side, and generate one output from it.

# EX:
# expression_to_be_evaluated logicaloperator expression_to_be_evaluated

# """

# place = "MCR"
# weather = "Cloudy"

# if place == "MCR" and weather == "Sunny":
#     print ("Check again")
# elif place == "MCR" and weather == "Rain":
#     print ("Obvs")
# else:
#     print ("What? Isn't it raining?")

# """
# The expressions either side of the logical operator are evaluated 

# Because we're using "and", either side needs to evaluate to be True to run

# The "place" variable matches “MCR”, but weather doesn't match in either condition. So the "else" statement will run.

# "and" allows us to write strict conditions that rely on more than one comparison. For example, you must get your username and your password correct to log in.
# """

# #---------------------------------------------------------------------------

# day = "Saturday"

# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend")
# else:
#     print("When is the weekend?")

# """
# The "or" logical operator evaluates if only one condition is True. If at least one matches, it will run the code.

# It allows us to have two or more options to trigger the same condition. And is much more efficient than writing out the same elif statement again and again.
# """

# #---------------------------------------------------------------------------

"""
LOGICAL OPERATOR "and":
True and True = True
True and False = False
False and False = False

LOGICAL OPERATOR "or":
True and True = True
True and False = True
False and False = False
"""
