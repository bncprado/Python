# """"

# If I asked you to print out each item in this list, how would you do it?

# """

# fav_drinks = [
#   "juice",
#   "tea",
#   "water"  
# ]

# """"
# You might approach the task this way.

# """
# print(fav_drinks[0])
# print(fav_drinks[1])
# print(fav_drinks[2])

# """
# But how efficient would this be if you had 1000 drinks in your list?

# Time to make the code work for us!

# """

# for i in fav_drinks:
#     print(i)

# """"
# This is a for loop. It iterates through a sequence, and runs the block for as many things as there are in that sequence.

# The program will run once but the loop will run three times; one time for each item in the list.

# "i" is the index variable. It's created by the "for loop", and each time the code runs, "i" changes to the next element in the sequence

# """

# for drink in fav_drinks:
#     print(drink) #We could call it anything. It's just a variable name.

# # "i" is very common, though, and easily recognisable in this context.

# for i in fav_drinks:
#     print("a great choice")

# """
# We don't need to reference "i" in our block if we don't need to. This loop will print “A great choice!” three times, once for each item in the list.
# """

# """"
# For loops:

# - iterate though a sequence 
# - execute a block of code for as many things as there are in the sequence 
# - run a finite amount of times. They will always eventually stop

# Does this mean if I want something to happen 1000 times, I have to have a list with 1000 items in?

# """

# #--------------------------------------------------------------------------------------------------

# # ITERATION IN CODING - RANGE

# for i in range(10):
#     print (i)

# """"
# Range generates a sequence for us to iterate through. 

# This loop will run 10 times. 

# What will we see printed?

# "range(10)" means the loop will happen 10 times but "i" will be the numbers 0-9

# Range needs 1 parameter, but is actually using 3.

# start , stop, step
# """

# for i in range (0,10,1): #start, stop, step. Same as using just 10
#     print (i)

# """
# 0 is our start point.

# 10 is our stop point, but we stop one step before it.

# 1 is our step. We count up by 1 each time we iterate

# Range only needs us to define the stop value. By default, we will start at 0 and count up by 1 each time.
# """
# #-----------------------------------------------------------------------------------------------------------


# """ What will this code print?  
#     A) 6, 7, 8, 9, 10, 11
#     B) 5, 6, 7, 8, 9, 10
#     C) 5, 6, 7, 8, 9, 10, 11

# """
# for i in range (5,11): # Without executing the code, I'd say 5 to 10 cause it includes the first and excludes the last
#     print(i)

# #----------------------------------------------------------------------------------------------------------------------

# """"  What will this print?

#       A) 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
#       B) 2, 4, 6, 8, 10, 12
#       C) 2, 4, 6, 8, 10
# """
# for i in range (2, 12, 2): # id say C without printing. Start 2, Stop 12, Step 2. 12 would be excluded anyway so it can't be B, and it can't be A cause it has step of 2 so odd numbers wouldn't count
#     print(i)
#     #I was right

# #----------------------------------------------------------------------------------------------------------------------

""" EXERCISE
Using range, find the total of adding the numbers 1 - 100
"""
total = 0

for i in range(101):
  total = total + i
  print(total)

