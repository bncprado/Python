## 1. Append Recap ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_names = []
for row in apps_data[1:]:
    name = row[1]
    apps_names.append(name)
    
print(apps_names[:5])
    
   
    

## 2. If Statements ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    # Complete the code from here
    price = float(row[4])
    if price == 0.0:
        free_apps_ratings.append(rating)
        
avg_rating_free = sum(free_apps_ratings)/len(free_apps_ratings)

## 3. Booleans ##

a_price = 1
print(a_price == 0)
print(a_price == 1)

## 4. If Statement Fundamentals ##

if False:
    print("2 + 2 == 5")
    print("lemons are sour")

if True:
    print("the sky is blue")
    print("5 >= 3")
    
if False:
    print("spheres have corners")
    print("7 / 5 == 2")

## 5. The Average Rating of Non-free Apps ##

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

## 6. The Average Rating of Gaming Apps ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_games_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    if genre != "Games":
        non_games_ratings.append(rating)
        
avg_rating_non_games = sum(non_games_ratings)/len(non_games_ratings)