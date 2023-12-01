from csv import reader
opened_file_ios = open('D:\Coding\Python\Learning\DataQuest.io - Data Science in Python\Opening CSV\AppleStore.csv', encoding='utf8')
opened_file_android = open('D:\Coding\Python\Learning\DataQuest.io - Data Science in Python\Opening CSV\googleplaystore.csv', encoding='utf8')
read_file_ios = reader(opened_file_ios)
read_file_android = reader(opened_file_android)
ios_data = list(read_file_ios)
android_data = list(read_file_android)

import numpy

ios_new = numpy.array(ios_data)

# print(ios_new[0]) #prints the entire row 0
# print(ios_new[0,0]) #prints the row 0, column 0
# print(ios_new[:,0]) #prints the entire column 0
# print(ios_new[:,:]) #prints all rows and columns
# print(ios_new[:1,:10]) #prints row 0, columns from 0 to 9
# print(ios_new[:3,:3]) #prints row 0 to 2, columns from 0 to 2
# print(ios_new[:,[1,4,5]]) #prints all rows, columns from 1,4 and 5

