print("""

Copy out the list. Use a method to find out how many of the following items I’ve ordered:

egg 
kale 
stamps 
carrot 
orange 
juice
""")
      
shopping_list = [
    'apple',
    'carrot',
    'pizza',
    'carrot',
    'dog food',
    'orange juice',
    'egg',
    'kale',
    'carrot',
    'kale',
    'orange juice', 
    'kale', 
    'toilet roll', 
    'stamps',
    'noodles', 
    'pasta sauce',
    'egg', 
    'pasta sauce'
    ]

print(f"""Eggs: {shopping_list.count('egg')}
Kale: {shopping_list.count('kale')}
Stamps: {shopping_list.count('stamps')}
Carrots: {shopping_list.count('carrot')}
Orange Juice: {shopping_list.count('orange juice')}
""")
