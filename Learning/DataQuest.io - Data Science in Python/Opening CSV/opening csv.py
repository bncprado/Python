from csv import reader
opened_file = open("D:\Coding\Python\Learning\DataQuest.io - Data Science in Python\Opening CSV\AppleStore.csv", encoding='utf8')
read_file = reader(opened_file)
apps_data = list(read_file)

print(apps_data[:1])

