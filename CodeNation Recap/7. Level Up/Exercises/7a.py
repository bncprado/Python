""" 
ACTIVITY

Create a shop dictionary, listing item as the key and the price as the value

Create a program which allows users to purchase from you store. Users should be able to input the item they want, and how many of them they wish to buy. 

Display a total cost from this information. 

Allow the user to keep purchasing items from your shop until they are done. Update the total as necessary
"""


import datetime

shop_list = {
    'Apple': 0.99,
    'Banana': 0.5,
    'Orange': 0.75,
    'Milk': 2.49,
    'Bread': 1.99,
}

current_time = datetime.datetime.now().time().hour

def greetings():
    if current_time >= 0 and current_time < 12:
        print ("\nGood morning. Welcome to Bruno Groceries.\n")
    elif current_time >= 12 and current_time < 18:
        print ("\nGood afternoon. Welcome to Bruno Groceries.\n")
    else:
        print ("\nGood evening. Welcome to Bruno Groceries.\n")

def items_list():
    print("Here are the items we have available today\n")
    print("ITEMS    \tPRICE\n")
    for key, value in shop_list.items():
        print(f"{key}     \t£{value:.2f}")
    print("")

greetings()

items_list()

shop_cart_items = []

while True:
    shop_cart_items.append(input("Type the item you want to buy: ").capitalize())
    try:
        answer = input("Would you like to add more items? Type \"Yes\" or \"No\": ".lower())
        answer == "yes" or answer == "no"
        break
    except:
        ("Please, type \"Yes\" or \"no\"")

print(shop_cart_items)