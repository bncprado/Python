# """"
# Learning Objectives

# } To understand the difference between the built in library, imported libraries, and installed libraries 

# } To be able to use imported libraries to improve code functionality 

# } To understand package managers

# """

# """

# Everything we've been doing so far has been using the Python standard or built-in library.

# This is the collection of objects, methods, modules, and functions which make Python work as it does.

# Python is a versatile language, and we've done a lot with the built in library already! When you installed Python, you also installed a number of other Python libraries.

# They contain a lot of very useful bits of code that can provide you with lots of functionality.

# """

# """"
# Let's make a random number game! 

# I'm going to pick a number, and get the program to keep guessing numbers until it guesses mine.

# How can we do this?

# """

# import random

# """"
# Generating random numbers is something that happens often enough that Python comes with a random library. But not often enough to have it built-in. Instead, we must import it

# After importing this, we have access to many more methods!

# We can access them with dot notation.
# """

# print(random.random())

# """"
# Run this code a number of times. What do you notice about what is generated?

# random.random() generates a random float between 0 and 1.
# """

# print(random.uniform(1,10))

# """
# random.uniform(a,b) takes two parameter: a lower and an upper bound and generates a random float.

# It includes a, but might stop before b, depending on rounding.

# """

# print(random.randint(1,10))

# """"
# random.randint(a,b) takes two parameter: a lower and an upper bound and generates a random integer inclusive of the two bounds.

# """

# #--------------------------------------------------------------------------------------------------------------------

# """"
# We can use these libraries to save us a lot of time. Creating a random number game is much easier when I don't have to worry about how to create the randomness.
# """

# import random

# my_num = 13
# ran_num = random.randint(1,50)

# while my_num != ran_num:
#     print(f"The number {ran_num} doesn't match my number {my_num}")
#     ran_num = random.randint(1,50)

# print(f"The number {ran_num} matches my number {my_num}")

# #--------------------------------------------------------------------------------------------------------------------

# """
# There are two ways we can import libraries. The whole library and we access all the methods with dot notation or e can just import the modules we need from a library. 

# When we do so, we don't need to use dot notation anymore. We just use the module name.

# Both are going to do the same thing generate a random float. It's generally better to just import what you need.

# """

# from random import uniform

# print(uniform(1,10))

# import random

# print(random.uniform(1,10))

# #--------------------------------------------------------------------------------------------------------------------
