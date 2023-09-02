## 1. Multiple Conditions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    # Complete code from here
    if price == 0.0 and genre == "Games":
        free_games_ratings.append(rating)
        
avg_rating_free_games = sum(free_games_ratings)/len(free_games_ratings)

## 2. The or Operator ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    # Complete code from here
    if genre == "Social Networking" or genre == "Games":
        games_social_ratings.append(rating)
        
avg_games_social= sum(games_social_ratings)/len(games_social_ratings)      
    

## 3. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_social_ratings = []
paid_games_social_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price == 0:
        free_games_social_ratings.append(rating)
        
    if (genre == 'Social Networking' or genre == 'Games') and price > 0:
        paid_games_social_ratings.append(rating)
        
    
        
avg_free = sum(free_games_social_ratings) / len(free_games_social_ratings)

# Not-free apps (average)
avg_not_free = sum(paid_games_social_ratings) / len(paid_games_social_ratings)

## 4. Comparison Operators ##

x = -6
y = 14
z = 8.5

if x > z:
    print("x is greater than z")
    
if y != z:
    print("y is not equal to z")
    
if z > x and z < y:
    print("z is between x and y")

## 5. Comparison Operator Applications ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_higher_than_9 = []
n_apps_less_9 = []
n_apps_more_9 = []
for row in apps_data[1:]:
    price = float(row[4])
    rating = float(row[7])
    if price >= 9:
        apps_higher_than_9.append(rating)
    if price > 9:
        n_apps_more_9.append(rating)
    if price <= 9:
        n_apps_less_9.append(rating)

avg_rating = sum(apps_higher_than_9)/len(apps_higher_than_9)  
n_apps_less_9 = len(n_apps_less_9)
n_apps_more_9 = len(n_apps_more_9)

## 6. The else Clause ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append("free")
    else:
        app.append("not free")

apps_data[0].append("free_or_not") 

print(apps_data[:6])

## 7. The elif Clause ##

app_ratings = [['Facebook', 3.5], ['Notion', 4.0], ['Astropad Standard', 4.5], ['NAVIGON Europe', 3.5]]

for row in app_ratings:
    rating = row[1]
    if rating < 3.0:
        row.append('below_average')
    elif rating >= 3.0 and rating < 4.0:
        row.append('roughly average')
    else:
        row.append('better than average')

## 8. Else vs. elif ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0:
        app.append("free")
    elif price > 0 and price < 20:
        app.append("affordable")
    elif price >= 20 and price < 50:
        app.append("expensive")
    else: 
        app.append("very expensive")
        
apps_data[0].append('price_label')            