# years = [1999, 2999]
# words = ['test', 'bruschetta']
# cities = ['london', 'paris']
# list = [[1999, 2999], ['test', 'bruschetta'], ['london', 'paris']]
# for row in list:
#   print (row[1])

#########################################

# content_ratings = {
#     "PG-13": 10,
#     "R": 5,
#     "G": 3
# }

# # c_rating = "PG-13"
# # content_ratings["PG-13"] = content_ratings["PG-13"]+1

# # print(content_ratings)

# # apple = 13
# # apple = apple + 1
# # apple +=1
# # print (apple)

# content_ratings["B"]=2
# print(content_ratings)

############################################## ADDING AND REMOVING ITEMS TO DICTIONARIES 

# dict = {}
# dict["novo"]= "novo string"
# print(dict)
# dict.clear()
# print(dict)
# dict["novo"]= "novo string"
# dict["velho"]= "velho"
# dict.pop("novo")
# print(dict)


############################################### ASSIGMENT OPERATORS TEST

# number = 1
# number += 2
# print (number)

############################################### 

# number1 = 1
# number3 = 3

# if 1 < 2 >= 4:
#   print('opa')
# else:
#   print('n')

############################################### FUNCTIONS

# def soma(number, number2):
#   lista = [number,number2, number]
#   return print(sum(lista))

# soma(1,2)
  

############################################## MORE FUNCTIONS

# def onenumber(number):
#   return number

# def twonumbers(number1, number2):
#   return number1, number2

# print(type(onenumber(1))) #output: int
# print(type(twonumbers(1,2))) #output: tuple

############################################## TUPLES
# a_tuple = (1,2)
# also_a_tuple = 1,2

# print(type(a_tuple)) #output: <class 'tuple'>
# print(type(also_a_tuple)) #output: <class 'tuple'>

# # Every time we create a variable with values separated by comma (,), it'll automatically create a tuple.

# def new_func(number1, number2):
#   return number1, number2 #it will automatically return a tuple, cause we separated the values by a comma

# print(type(new_func(1,2))) #output: <class 'tuple'>

# def new_func(number1, number2): #now, the function new_func was redefined and it's returning a list
#   return [number1, number2]

# print(type(new_func(1,2))) #output: <class 'list'>

############################################## MORE ABOUT TUPLES

# tuple3rd = 1,2,3,4
# one, two, three, four = tuple3rd #that's the same as one = tuple[0] and so on
# print(tuple3rd)
# print(one)
# print(two)
# print(three)
# print(four)
# one, two, three, four, five = tuple3rd
# print(five) #output: ... ValueError: not enough values to unpack (expected 5, got 4)

############################################## MORE ABOUT TUPLES #we can use the same technique to unpack lists

# a_list = [0,1,2,3]
# zero, one, two, three = a_list #that's the same as zero = a_list[0] and so on
# print(a_list)
# print(zero)
# print(one)
# print(two)
# print(three)

############################################## Loop in lists of lists
# list_of_lists = [['name', 'age', 'nationality'],['Bruno', 'fourty-two', 'Brazilian']]

# for row in list_of_lists:
#   print(row[0])

##############################################
# vazia=[]
# lista = [['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up'],['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up'],['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up'],['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up'],['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']]

# print(len(lista))
# for row in lista:
#   name = row[0]
#   review = row[3]
#   if name == 'Photo Editor & Candy Camera & Grid & ScrapBook' and name not in vazia:
#     vazia.append(row)

# print(len(vazia))
###############################################

# name = 'Instachat 😜'

# for x, y, z in name, name, name:
#   print(x)
#   print(y)
#   print(z)


# def check_char(string):
#     for x in string:
#         if ord(x) > 127:
#             return False
#     return True

# print(check_char(name))

# fruits_prices = {
#     'watermelon': 3.00,
#     'apple': 1.00,
#     'banana': 0.75,
#     'orange': 1.25,
#     'grape': 2.50,
#     }

# print(sorted(fruits_prices))

############################################### split method

# name = '1957-1959'
# name = name.split('-') #it removes the chosen char and splits the rest into a list
# print(name)

############################################### converting list of strings to int

# name = '1957-1959'
# name = name.split('-') #it removes the chosen char and splits the rest into a list
# soma=0
# for x in name:
#   x=int(x)
#   soma+=x

# soma= round(soma/len(name))

# print(soma)

############################################### using type in if statements

# number = 1

# # print(type(number))
# if isinstance(number, int):
#     print('deu certo')
# else:
#     print('fudeu')


############################################## for loop with dictionaries

# dict = {
#     'orange': 4,
#     'banana': 4,
#     'apple': 2
# }

# for x in dict:
#   print(x)
# """OUTPUT:
# orange
# banana
# apple
# """

# print(dict.items()) #OUTPUT: dict_items([('orange', 4), ('banana', 4), ('apple', 2)])

# for key, value in dict.items():
#       print(f"{key} = {value}")



# ############################################### merging lists

# list1 = [1,2,3]
# list2 = [4,5,6]
# merged = list1+list2

# print(merged) #OUTPUT: [1, 2, 3, 4, 5, 6]
