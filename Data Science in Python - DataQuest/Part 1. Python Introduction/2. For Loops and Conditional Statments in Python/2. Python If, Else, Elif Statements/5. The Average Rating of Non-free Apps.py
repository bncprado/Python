"""
In the diagram below, we created a list of lists named app_and_price, and we want to extract the names of the free apps in a separate list. To do that, complete the following:

- Create an empty list named free_apps.
- Iterate over app_and_price. For each iteration, we do the following:
    - Extract the name of the app and assign it to a variable named name.
    - Extract the price of the app and assign it to a variable named price.
    - Append the name of the app to free_apps (the empty list that we initialized outside the loop) if the price of the app equals 0.

CODE:
app_and_price = [['Facebook', 0], ['Instagram', 0], ['Plants vs. Zombies', 0.99], ['Minecraft: Pocket Edition', 6.99], ['Temple Run', 0], ['Plague Inc.', 0.99]]

free_apps = []
for app in app_and_price:
    name = app[0]
    price = app[1]

    if price == 0:
        free_apps.append(name)

print(free_apps)

Output
['Facebook', 'Instagram', 'Temple Run']

The example above will help us understand what we did on the first screen of this lesson, where we extracted only the ratings of free apps. The steps we took above are the same as the ones we took on the first screen when we used this snippet of code:

CODE:
ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
​
    if price == 0.0:
        ratings.append(rating)

Explain

Copy
Above, we completed the following:

Looped through a list of lists named apps_data. For every iteration, we completed the following:
Extracted the rating of the app as a float and assigned it to a variable named rating.
Extracted the price of the app as a float and assigned it to a variable named price.
Appended the rating of the app to ratings (an empty list that we initialized outside the loop) if the price of the app equals 0.
After we extracted the ratings of the free apps in a separate list, we computed the average value by adding up all the ratings in that list and dividing the sum by the length of the list. However, we still need to compute the average rating for non-free apps.

When we isolated the free apps, we used the condition "if the price is equal to 0.0" (if price == 0.0) to isolate the non-free apps. Change the condition to "if the price is not equal to 0.0." For "is equal to," we can use the operator ==. For "is not equal to," we'll need to use the != operator.

Below, we see an example of the != operator in use:

img
Let's also look at an example where we use a variable (price, in the example below) with the != operator:

img
In the exercise below, we're going to compute the average rating of non-free apps. In the code editor on the right, we've already added the code we wrote on the first screen of this lesson to compute the average rating of free apps.

Instructions

Modify the existing code in the editor on the right to compute the average rating of non-free apps.

  1. Change the name of the empty list from free_apps_ratings to non_free_apps_ratings (the list we defined before the for loop).
  2. Change the condition if price == 0.0 to account for the fact that we now want to isolate only the ratings of non-free apps.
  3. Change free_apps_ratings.append(rating) to make sure the ratings are appended to the new list non_free_apps_ratings.
  4. Compute the average value by adding up the values in non_free_apps_ratings and dividing by the length of this list. Assign the result to avg_rating_non_free.
  5. Optional exercise: Inspect the value of avg_rating_non_free and compare the average with the free apps (the average rating of free apps is approximately 3.38 — we computed it on the first screen). Can we use the average values to determine whether free apps are better than non-free apps?

GIVEN CODE:


# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price == 0.0:
        free_apps_ratings.append(rating)
    
avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)

"""

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price != 0.0:
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

avg_rating_free = 3.38

if avg_rating_free > avg_rating_non_free:
    print("Free apps have a better rating score than paid apps")
else:    
    print("Paid apps have a better rating score than free apps")
