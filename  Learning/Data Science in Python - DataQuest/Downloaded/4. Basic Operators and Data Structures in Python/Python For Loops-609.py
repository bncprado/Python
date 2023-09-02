## 2. For Loops ##

app_names = ['Facebook', 'Instagram', 'Clash of Clans', 'Fruit Ninja Classic', 'Minecraft: Pocket Edition']
for elements in app_names:
    print(elements)

## 3. For Loops Continued ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

for row in app_data_set:
    rating_count = row[3]
    print(rating_count)

## 4. For Loop Structure ##

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

## 5. The Average App Rating ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

rating_sum = 0

for each_row in app_data_set:
    rating = each_row[-1]
    rating_sum += rating
    print(rating_sum)

avg_rating = rating_sum / len(app_data_set)

## 6. Opening a File ##

from csv import reader

opened_file = open("AppleStore.csv")
read_file = reader(opened_file)
apps_data = list(read_file)

print(len(apps_data))
print(apps_data[0])
print(apps_data[1:3])

## 8. Dealing with Errors ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum=0
for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum += rating
    
avg_rating = rating_sum/len(apps_data[1:])

## 9. Alternative Method to Calculate an Average ##

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
    