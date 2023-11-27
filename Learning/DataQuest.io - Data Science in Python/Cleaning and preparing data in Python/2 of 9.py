''' 

Instructions

Use the open() function to open the artworks.csv file. Assign the result to opened_file.

Use the reader() function to parse the data from opened_file. Assign the result to read_file.

Use list() to convert read_file into a list of lists. Assign the result to moma.

Use list slicing to remove the column names (the first row) from the moma list of lists.

'''

##################################################   PROVIDED CODE (with the )

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('D:\Coding\Python\Learning\DataQuest.io - Data Science in Python\Cleaning and preparing data in Python\Artworks.csv', encoding='utf8')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
moma = list(read_file)

# remove the first row of the data, which
# contains the column names
moma = moma[1:]

print(moma[:5])
