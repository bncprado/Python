# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price*item1_quantity

# print(type(item1)) # <class 'str'>
# print(type(item1_price)) # <class 'int'>
# print(type(item1_quantity)) # <class 'int'>
# print(type(item1_price_total)) # <class 'int'>

###########################################################################################

# We can create our own datatype with OOP

class Item:
    pass

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1)) # <class '__main__.Item'>
print(type(item1.name)) # <class 'str'>
print(type(item1.price)) # <class 'int'>
print(type(item1.quantity)) # <class 'int'>