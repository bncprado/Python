""""
1. Our users liked the previous functionality that we added to our travel application, but recently we have had an influx of users planning trips in Italy. We want to create a small function to output the top places to visit in Italy. Another member of our team already started on the implementation of this feature but it is still missing a few key details.

Take a second to review the code and click Run when you are ready to move on. For now, there will be no output.
"""

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third
  

""""
2. We want to be able to return the three most popular destinations from our function top_tourist_locations_italy().

Add a line in the function top_tourist_locations_italy() that will return the values of first, second, third in that exact order.
"""

""""
3.In order to use our three returned values from top_tourist_locations_italy() we need to assign them to new variables names after we call our function.

Set the return of the function top_tourist_locations_italy() to be equal to three new variables called most_popular1, most_popular2, and most_popular3 in that exact order.
"""

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

""""
4. Use three print() statements to output the value of most_popular1, most_popular2, and most_popular3.
"""

print(most_popular1)
print(most_popular2)
print(most_popular3)
