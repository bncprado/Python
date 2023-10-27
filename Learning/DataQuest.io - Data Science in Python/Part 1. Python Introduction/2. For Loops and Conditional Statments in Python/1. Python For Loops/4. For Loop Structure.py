# #FOR LOOP STRUCTURE

# """iterable_list = [1,2,3]

# for iteration_variable in iterable_list:
#     print(iteration_variable)"""

# # We can use code that's outside the loop to interact inside the loop

# iterable_list = [1,3,5]

# sum = 0

# for iteration_variable in iterable_list:
#     sum += iteration_variable
#     print(sum)

# print(sum)#new and updated value after the loop

"""
Instructions

Calculate the total number of app ratings for the apps stored in the app_data_set variable.

1. Initialize a variable named rating_sum with a value of zero outside the loop body.

2. Loop (iterate) over the app_data_set list of lists. For each of the five iterations of the loop (for each row in app_data_set):
  - Extract the rating count of the app, and store it to a variable named rating_count.
  - Add the value stored in rating_count to the current value of rating_sum and assign the result back to rating_sum.
  - Print rating_sum.

GIVEN CODE

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

"""

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

rating_sum = 0

for each_row in app_data_set:
    rating_count = each_row[-2]
    rating_sum += rating_count
    print(rating_sum)