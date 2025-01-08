my_info = ('Bruno',44,'musician')
print(my_info)

#unpacking a tuple

name, age, occupation = my_info #the number of variables must match the number of elements in a tuple

print(f"My name is {name}, I'm {age} yo and in a {occupation}")

#one element tuple

one_element_tuple = (4)

print(type(one_element_tuple)) #it won't print a tuple. It must have a (trailing) comma after the first element, so python can identify it as a type tuple

one_element_tuple = (4,)

print(type(one_element_tuple))



