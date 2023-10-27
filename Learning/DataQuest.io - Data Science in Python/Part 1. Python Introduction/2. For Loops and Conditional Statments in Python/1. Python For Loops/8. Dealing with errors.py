"""
Learn
To address the errors, we need to convert strings to integers or floats (decimal numbers) using the int() or float() functions, respectively. The ratings are expressed as decimal points, so we'll convert them to floats using the float() function.

rating_sum = 0
for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum = rating_sum + rating
​
print(rating_sum)

Output
25383.5

This works! We've addressed the error. Let's complete the exercise.

Instructions

Calculate the average app rating for all the 7,197 apps stored in the dataset.

1. Initialize a variable named rating_sum with a value of zero.
2. Loop through the apps_data[1:] list of lists (make sure you don't include the header row). For each of the 7,197 iterations of the loop (for each row in apps_data[1:]), do the following:
  - Extract the rating of the app, and store it to a variable named rating (the rating has the index number 7). Convert the rating value from a string to a float using the float() function.
  - Add the value stored in rating to the current value of rating_sum and assign the result back to rating_sum.
3. Divide the rating sum (stored in rating_sum) by the number of ratings to get an average value. Store the result in a variable named avg_rating.

GIVEN CODE:

"""

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum=0
for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum += rating
    
avg_rating = rating_sum/len(apps_data[1:])
