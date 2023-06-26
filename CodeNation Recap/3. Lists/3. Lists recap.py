# #LIST SYNTAX:

# coffee_order = [
#     'Alex - Cortado', 
#     'Ben - Latte', 
#     "Charlie - Mocha"
# ]

# print(coffee_order)

# """ 

# Lists are stored within [] square brackets, with each item separated by a comma. To access the data inside the list, we use the variable name.

# The items don't need to be on a new line, but it does make it more readable.Even though we wrote the list in different lines, when printing we get everthing in the same line. 

# Each item in this case is a string they'll all need their own set of quote marks.

# """

# #-------------------------------------------------------------------------

# # INDEX IN LISTS

# """
# Like any good list, we can access individual items.

# How did we access individual characters in a string?

# Remember - Python is zero indexed. Collections start at 0, not 1!

# """
# coffee_order = [
#     'Alex - Cortado', 
#     'Ben - Latte', 
#     "Charlie - Mocha"
# ]

# print(coffee_order[2]) #result will be the third one in the list. ZERO indexed

# # IF YOU WANT TO REASSIGN AN ITEM IN THE LIST, it's the same as reassigning a string or a number in a variable

# print(coffee_order)

# coffee_order[1] = "Ben - Latte mas não morde"

# print(coffee_order)

# # Line 43 will show the list with Ben ordering a Latte, but from line 45 onwards, we’ve updated that item in list.

# #-------------------------------------------------------------------------

# Data, properties, and methods with lists

# Like strings, lists have associated methods we can use to manipulate them! Remember dot notation, object.method()

coffee_order = [
    'Alex - Cortado', 
    'Ben - Latte', 
    "Charlie - Mocha"
]

print(len(coffee_order))#show the number of items in the list, not the number of characters like it did on a string.

# HOW TO ADD ANOTHER ORDER TO SOMEONE NEW IN THE OFFICE? Using the .append() method, that add a new item at the end of the list.
coffee_order.append("Diane - Cappuccino")

print(coffee_order)

# HOW ABOUT REMOVING AN ITEM?

coffee_order.pop() #The .pop() method will remove the last item in our list

print (coffee_order)

coffee_order.pop(0) #or we can specify the index position of the item we'd like to remove

print (coffee_order) # "Alex - Cortado" was removed cause we ask .pop() method when we specified the indexed item number 0 (the first one)

