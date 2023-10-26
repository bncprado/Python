opened_file = open("D:\Coding\Python\ Learning\Data Science in Python - DataQuest\Opening CSV\AppleStore.csv")
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

print(apps_data[:5])

sds = "test"