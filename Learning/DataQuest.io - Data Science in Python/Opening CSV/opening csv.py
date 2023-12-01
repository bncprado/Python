from csv import reader
opened_file_ios = open('D:\Coding\Python\Learning\DataQuest.io - Data Science in Python\Opening CSV\AppleStore.csv', encoding='utf8')
opened_file_android = open('D:\Coding\Python\Learning\DataQuest.io - Data Science in Python\Opening CSV\googleplaystore.csv', encoding='utf8')
read_file_ios = reader(opened_file_ios)
read_file_android = reader(opened_file_android)
ios_data = list(read_file_ios)
android_data = list(read_file_android)


# print(len(ios_data))


# if 'Installs' in android_data[0]:
#   print('\nyes\n')

# del android_data[0]

# if 'Installs' in android_data[0]:
#   print('NOT ANYMORE')


# import string

# roman_characters = list(string.ascii_uppercase)

# non_roman = "爱奇艺"
# a = []

# for row in roman_characters:
#   if non_roman not in roman_characters:
#     a.append(non_roman)
  
# print(a)

# for row in ios_data[:1]:
#   name = row[1]
#   print(name)

# def explore_data(dataset, start, end, rows_and_columns=False):
#     dataset_slice = dataset[start:end]    
#     for row in dataset_slice:
#         print(row)
#         print('\n') # adds a new (empty) line after each row

#     if rows_and_columns:
#         print('Number of rows:', len(dataset))
#         print('Number of columns:', len(dataset[0]))


import numpy

ios_data = numpy.array(ios_data)

print(ios_data.diagonal())

print(ios_data[0:1])

# free_ios_apps = []
# for row in ios_data[1:]:
#     if float(row[4]) == 0.0:
#         free_ios_apps.append(row)
# explore_data(free_ios_apps,0,2, True)     

# free_android_apps = []
# paid_android_apps = []
# else_android_apps = []
# for row in android_data[1:]:
#     if row[6] == 'Free':
#         free_android_apps.append(row)
#     elif row[6] == 'Paid':
#         paid_android_apps.append(row)
#     else:
#         else_android_apps.append(row)

# explore_data(free_android_apps,0,2,True)

# free_android_apps.append(else_android_apps[0])
# free_android_apps.append(else_android_apps[1])
# print(free_android_apps[-1])

# explore_data(free_android_apps,0,2,True)

# def has_non_roman_chars(input_list):
#     for item in input_list:
#         if any(ord(char) < 0x0020 or ord(char) > 0x007F for char in item):
#             return True
#     return False

# names = []
# for row in free_android_apps:
#     names.append(row[0])

# print(names)
# # non_english_names = []

# # # Example usage:
# contains_non_roman = has_non_roman_chars(names)

# print(contains_non_roman)

# for row in names:
#     if contains_non_roman


# # if contains_non_roman:
# #     print("The list contains non-Roman characters.")
# # else:
# #     print("The list only contains Roman characters.")