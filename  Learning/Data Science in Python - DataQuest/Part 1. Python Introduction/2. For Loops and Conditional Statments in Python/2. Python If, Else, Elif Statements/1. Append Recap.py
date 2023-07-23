"""
In this lesson on conditional statements, we'll learn how to ask more advanced questions about datasets, by using the following tools:

 - How to use if statements
 - How to use Boolean values
 - How to use comparison operators with strings or lists

Let's work with a dataset that stores information for 7,197 mobile apps and we'll ask questions like the following (in regard to average ratings):

 - What's the average rating of non-free apps?

 - What's the average rating of free apps?

To answer these two questions, we need to find a way to separate free apps from non-free or purchase apps, because they are all listed together in our dataset. We must specifically complete the following:

 - Isolate the ratings for free and non-free apps in separate lists.
 - Compute the average rating for each list.

Before we isolate the ratings for the free apps, let's look at how to use the list_name.append() function to extract the ratings into a separate list. In the code below, complete the following:

 - Convert the AppleStore.csv file into a list of lists and assign that list to a variable named apps_data.
 - Create an empty list named ratings.
 - Iterate over apps_data[1:] (which excludes the header row), and for each iteration (row), we do the following:
   - Extract the rating and convert it to a float using float(row[7]). The rating has the index number 7 and comes as a string, so we need to convert it to a float.
   - We assign the rating to a variable named rating.
   - We append rating to the ratings list we created outside the loop using ratings.append(rating) function.


The problem with this approach is that it includes all the ratings for both free and non-free apps. To isolate only the ratings of the free apps, we need to add a condition to our code. We'll learn about conditions next. For now, let's practice working with the list_name.append() function.

Instructions

Complete the code in the editor to find the names for all of the apps in the dataset. The AppleStore.csv is available under the csv tab in the editor to the right.

1. Inside the for loop, complete the following:
 - Assign the name of an app to a variable called name. The name is the second element in each row (the index starts at 0).
 - Append the value stored in name to the apps_names list using the list_name.append() function (note the apps_names list is already defined in the code editor) and be careful with indentation.

2. Print the first 5 elements in apps_names list to display the names of the apps.
"""

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_names = []
for row in apps_data[1:]:
    name = row[1]
    apps_names.append(name)
    
print(apps_names[:5])