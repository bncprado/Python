#

""" 
ACTIVITY

Create a shop dictionary, listing item as the key and the price as the value

Create a program which allows users to purchase from you store. Users should be able to input the item they want, and how many of them they wish to buy. 

Display a total cost from this information. 

Allow the user to keep purchasing items from your shop until they are done. Update the total as necessary
"""

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
    print("Here are the items we have available today:\n")
    print("ITEMS    \tPRICE\n")
    for key, value in shop_list.items():
        print(f"{key}     \t£{value:.2f}")
    print("")

greetings()

items_list()

shop_cart_items = []
quantity = 0

while True:
    while True:
        what_want_to_buy = input("Please, type what you'd like to buy: ").capitalize()
        if what_want_to_buy not in shop_list:
            print(f"{what_want_to_buy} is not in the list, please type it again.")
        else:
            break
    while True:
        try: 
            how_many = int(input(f"Type the number of {what_want_to_buy.lower()}s you'd like to buy: "))
            break
        except:        
            print("Please, type a number: ")
    print(f"The total for {how_many} {what_want_to_buy.lower()}s is £{shop_list[what_want_to_buy]*how_many:.2f} ")

    break
print(shop_cart_items)
    
# if what_want_to_buy in shop_list:
#     shop_cart_items.append(what_want_to_buy*how_many)
#     print(shop_cart_items)
# else:
#     print("Item not in list")
#     print(shop_cart_items)
#     quit()

