"""
Instructions

Use the technique we've learned to print all app rating counts in the app_data_set list of lists. We've provided this list of lists in the code editor to the right.

Loop (iterate) over the app_data_set list of lists. For each of the five iterations of the loop (for each row in app_data_set):
Extract the rating count of the app and store it to a variable named rating_count. The rating count is the fourth element of each row (row[3]).
Print rating_count.

CODE GIVEN

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

"""

row_1 = ['Facebook' ,                 0.0,  'USD', 2974676, 3.5]
row_2 = ['Instagram',                 0.0,  'USD', 2161558, 4.5]
row_3 = ['Clash of Clans',            0.0,  'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic',       1.99, 'USD', 698516,  4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012,  4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
app_data_set2 = [['Facebook' ,                 0.0,  'USD', 2974676, 3.5],
                 ['Instagram',                 0.0,  'USD', 2161558, 4.5],
                 ['Clash of Clans',            0.0,  'USD', 2130805, 4.5],
                 ['Fruit Ninja Classic',       1.99, 'USD', 698516,  4.5],
                 ['Minecraft: Pocket Edition', 6.99, 'USD', 522012,  4.5]]

for row in app_data_set2:
    rating_count = row[:-4]
    print(rating_count)
