# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price*item1_quantity

# print(type(item1)) # <class 'str'>
# print(type(item1_price)) # <class 'int'>
# print(type(item1_quantity)) # <class 'int'>
# print(type(item1_price_total)) # <class 'int'>

###########################################################################################

# # We can create our own datatype with OOP

# class Item:
#     pass

# item1 = Item()
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

# print(type(item1)) # <class '__main__.Item'>
# print(type(item1.name)) # <class 'str'>
# print(type(item1.price)) # <class 'int'>
# print(type(item1.quantity)) # <class 'int'>

###########################################################################################

# How to create methods and execute them on our instances

# class Item:
#   def calculate_total_price(self, x, y): # when you create a function inside an object, we call them METHODS.
#     return x*y


# item1 = Item()
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))

# item2 = Item()
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3
# print(item2.calculate_total_price(item2.price, item2.quantity))
 
###########################################################################################

# class Item:
#   def __init__(self):
#     print("I AM CREATED")
#   def calculate_total_price(self, x, y): # when you create a function inside an object, we call them METHODS.
#     return x*y


# item1 = Item()
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

# item2 = Item()
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3

###########################################################################################

# class Item:
#   def __init__(self, name):
#     print(f"An instance created: {name}")
#   def calculate_total_price(self, x, y): # when you create a function inside an object, we call them METHODS.
#     return x*y

# item1 = Item("Phone")
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

# item2 = Item("Laptop")
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3

###########################################################################################

# class Item:
#   def __init__(self, name):
#     self.name = name
#   def calculate_total_price(self, x, y): # when you create a function inside an object, we call them METHODS.
#     return x*y

# item1 = Item("Phone")
# item1.price = 100
# item1.quantity = 5

# item2 = Item("Laptop")
# item2.price = 1000
# item2.quantity = 3

# print(item1.name)
# print(item2.name)

###########################################################################################

# class Item:
#   def __init__(self, name, price, quantity):
#     self.name = name
#     self.price = price
#     self.quantity = quantity

#   def calculate_total_price(self, x, y): # when you create a function inside an object, we call them METHODS.
#     return x*y

# item1 = Item("Phone", 100, 5)

# item2 = Item("Laptop", 1000, 3)

# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)

###########################################################################################

# class Item:
#   def __init__(self, name, price, quantity=0):
#     self.name = name
#     self.price = price
#     self.quantity = quantity

#   def calculate_total_price(self, x, y): # when you create a function inside an object, we call them METHODS.
#     return x*y

# item1 = Item("Phone", 100)

# item2 = Item("Laptop", 1000)

# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)

###########################################################################################

# class Item:
#   def __init__(self, name, price, quantity=0):
#     self.name = name
#     self.price = price
#     self.quantity = quantity

#   def calculate_total_price(self): # when you create a function inside an object, we call them METHODS.
#     return self.price * self.quantity

# item1 = Item("Phone", 100, 1)

# item2 = Item("Laptop", 1000, 3)

# item2.has_numpad = False # attribute assignment  

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

###########################################################################################

# class Item:
#   def __init__(self, name, price, quantity=0):
#     self.name = name
#     self.price = price
#     self.quantity = quantity

#   def calculate_total_price(self): # when you create a function inside an object, we call them METHODS.
#     return self.price * self.quantity

# item1 = Item("Phone", "100", 1)

# item2 = Item("Laptop", "1000", 3)

# item2.has_numpad = False # attribute assignment  

# print(item1.calculate_total_price()) # 100
# print(item2.calculate_total_price()) # 100010001000

###########################################################################################

# SPECIFYING A TYPE and forcing it

class Item:
  def __init__(self, name: str, price: float, quantity=0): #When we pass float, it's ok to use integers. For quantity, we don't have to specify the data type cause we already passed an "int" so Python will assume it must be an "int" automatically

    assert name != str(name), f"the name must be a string"
    assert price != float(price), f"the price must be a number with two decimals"
    assert quantity != int(quantity), f"Quantity must be an integer number"

    self.name = name
    self.price = price
    self.quantity = quantity

  def calculate_total_price(self): # when you create a function inside an object, we call them METHODS.
    return self.price * self.quantity

item1 = Item(1, "100", 1) # I still can pass a different value

item2 = Item("Laptop", "1000", 3)

item3 = Item(1, "name", 1.11)

