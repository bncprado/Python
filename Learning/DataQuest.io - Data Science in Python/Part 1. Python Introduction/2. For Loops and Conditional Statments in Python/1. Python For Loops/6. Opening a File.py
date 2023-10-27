"""This lesson required csv files that weren't downloadable. So all the problems were solved inside the coding area in the lesson on the website"""

#Code 

from csv import reader

opened_file = open("/AppleStore.csv")
read_file = reader(opened_file)
apps_data = list(read_file)

print(len(apps_data))
print(apps_data[0])
print(apps_data[1:3])