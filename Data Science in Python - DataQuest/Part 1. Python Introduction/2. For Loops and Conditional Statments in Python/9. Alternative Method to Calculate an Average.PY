"""
Learn

Now we'll learn an alternative method for calculating the average rating value. Once we create a list, we can add (or append) values to it using the append() function. Let's take a look:

a_list = [1, 2]
a_list.append(3)
print(a_list)

Output
[1, 2, 3]

Here's how to append values to an empty list:

empty_list = []
empty_list.append(12)
print(empty_list)

Output
[12]

Unlike other functions we've learned, append() has a special syntactical usage, following the pattern list_name.append() rather than simply append() (we'll examine this syntactical quirk once we learn about functions and methods). Let's take another look:

list_1 = []
list_2 = [5, 's', 1]
​
list_1.append('data')
list_2.append(1.6)
​
print(list_1)
print(list_2)

Output
['data']
[5, 's', 1, 1.6]

Now that we know how to append values to a list, we can take the following steps to calculate the average app rating:

1. We initialize an empty list.
2. We start looping over our dataset and extract the ratings.
3. We append the ratings to the empty list we created in step one.
4. Once we have all the ratings, we do the following:
  - Use the sum() function to add all the ratings (to be able to use sum(), we'll need to store the ratings as floats or integers).
  - Divide the sum by the number of ratings (which we can get using the len() function).

Below, we can see these steps for our dataset containing five rows:

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]
​
app_data_set = [row_1, row_2, row_3, row_4, row_5]
​
rating_sum = [] # Step 1
for row in app_data_set:
    rating = row[-1] # Step 2
    rating_sum.append(rating) # Step 3
​
print(rating_sum)
​
avg_rating = sum(rating_sum) / len(rating_sum) # Step 4
print(avg_rating)

Output
[3.5, 4.5, 4.5, 4.5, 4.5]
4.3

Instructions

Using the new technique we've learned, calculate the average app rating for all of the 7,197 apps stored in our dataset.

1. Initialize an empty list named rating_sum.

2. Loop through the apps_data[1:] list of lists (don't include the header row). For each of the 7,197 iterations of the loop, do the following:
  - Extract the rating of the app, and store it to a variable named rating (the rating has the index number 7). Convert the rating value from a string to a float.
  - Append the value stored in rating to the list rating_sum.

3. Calculate the sum of all ratings using the sum() function.

4. Divide the sum of all ratings by the number of ratings, and assign the result to a variable named avg_rating.

5. Print the results of avg_rating.

GIVEN CODE

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

"""

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = []

for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum += [rating]

avg_rating = sum(rating_sum)/len(apps_data[1:])

print (avg_rating)