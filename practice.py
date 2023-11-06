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

a_list = [0,1,2,3]
zero, one, two, three = a_list #that's the same as zero = a_list[0] and so on
print(a_list)
print(zero)
print(one)
print(two)
print(three)

