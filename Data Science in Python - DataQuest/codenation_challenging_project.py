#importing "datetime" library to get time and use in our "greetings function"
import datetime 

#empty shop cart that will be updated as user type what they want to add
shop_cart = {}

# items we have available in our shop
shop_inventory = {
    'Apple': 0.99,
    'Banana': 0.5,
    'Orange': 0.75,
    'Milk': 2.49,
    'Bread': 1.99,
}

#this variable gets current time of the day to be used in the greetings function
current_time = datetime.datetime.now().time().hour

name = input("Please, tell us your name: ")

# this function gets the time of the day and print the appropriate greeting for the current time
def greetings():
    if current_time >= 0 and current_time < 12:
        print (f"\nGood morning {name}. Welcome to Bruno Groceries.\n")
    elif current_time >= 12 and current_time < 18:
        print (f"\nGood afternoon {name}. Welcome to Bruno Groceries.\n")
    else:
        print (f"\nGood evening {name}. Welcome to Bruno Groceries.\n")

# function that shows the user the available items and their prices in a friendly-reading table
def items_list():
    print("\nHere are the items we have available today:\n")
    print("ITEMS    \tPRICE\n")
    for key, value in shop_inventory.items():
        print(f"{key}     \t£{value:.2f}")
    print("")

greetings()

items_list()


while True: #the entire loop for adding products to the shop_list 
    while True: 
        which_item = input("\nPlease type the item you want to buy: ").capitalize()
        if which_item not in shop_inventory:
            print(f"\nSorry {name}, we don't have {which_item} today. Please, try something from our inventory.")
            items_list()
        else:
            break
    while True:
        try: 
            how_many = int(input(f"\nHow many {which_item}s would you like to buy {name}? "))
            break
        except:
            print(f"I'm sorry {name} but you have to type a number: ")
    if which_item in shop_cart:
        shop_cart[which_item] += how_many
    elif which_item not in shop_cart:
        shop_cart[which_item.capitalize()] = how_many  
    print("")
    print("ITEMS\t\tQTY\t\tTOTAL PRICE\n")
    overall_total = 0
    for key, value in shop_cart.items():
        print(f"{key}\t\t{value}\t\t£{shop_inventory[key]*value:.2f}")
        overall_total += shop_inventory[key]*value
    print(f"\nOVERALL TOTAL: £{overall_total:.2f}")
    print("")

    x = input(f"Do you want to keep shopping {name}?\nType \"Y\" then ENTER to keep shopping or anything else to go for payment: ").capitalize()
    if x == "Y":
        print("")
        items_list()
        continue
    else:
        break

print(f"""
THE TOTAL FOR YOUR BASKET IS £{overall_total:.2f}.

Thank you for shopping with us, {name}.""")

if current_time >= 0 and current_time < 12:
        print ("\nHave a great day.\n")
elif current_time >= 12 and current_time < 18:
        print ("\nEnjoy your afternoon.\n")
else:
    print ("\nHave a good evening\n")


