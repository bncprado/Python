#This file is just replicating the study of lists on codecademy

heights = [61, 70, 67, 64]
heights.append(65)
print(heights)

broken_heights = [65,71,59,62]

#Add any additional string to the end of the list ints_and_strings.

ints_and_strings = [1, 2, 3, "four", "five"]

ints_and_strings.append("string")

"""
Create a new list called sam_height_and_testscore that contains:
The string "Sam" (to represent Sam’s name)
The number 67 (to represent Sam’s height)
The float 85.5 (to represent Sam’s score)
The boolean True (to represent Sam passing the test)
Make sure to write the elements in exact order.
"""

sam_height_and_testscore = ["Sam",67,85.5,True]

"""
Create an empty list and call it my_empty_list. Don’t put anything in the list just yet.
"""

my_empty_list = []

"""
Jiho works for a gardening store called Petal Power. Jiho keeps a record of orders in a list called orders.

Use print to inspect the orders he has received today.
"""

orders = ["daisies", "periwinkle"]
print(orders)

"""
Jiho just received a new order for "tulips". Use append to add this string to orders.
"""

orders.append("tulips")
orders.append("roses")
print(orders)

"""
Jiho is updating a list of orders. He just received orders for "lilac" and "iris".

Create a list called new_orders that contains our new orders.
"""

new_orders = ["lilac","iris"]

"""
Use + to create a new list called orders_combined that combines orders with new_orders.
"""

orders_combined = orders + new_orders

"""
If you run this code, you’ll get an error:
"""

#broken_prices = [5, 3, 4, 5, 4] + 4

"""
Fix the command by inserting brackets ([ and ]) so that it will run without errors.
"""

broken_prices = [5, 3, 4, 5, 4] + [4]

""""
Use square brackets ([ and ]) to access the 4th employee from the list employees. Save it to the variable employee_four.
"""

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]