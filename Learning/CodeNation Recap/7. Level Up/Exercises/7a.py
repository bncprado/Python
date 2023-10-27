# PERSONAL CONSIDERATIONS

# I wasn't able to execute this project on my own when studying on my first Python Bootcamp. Everything was blurry and confused at that time. Now, 4 months later after studying everyday, I was able to finish this project by myself, without any help from chatGPT. The logic was difficult and took me 4 days to figure out. 
# I know this is a very simple project, but I'm very proud, specially considering that I'm basically a self-learner. 
# The challenge is not only learning how to code, but technical English for someone that doesn't speak English as first language is also very challenging. 
# When will I be able to find a job in Python? Today is 20th of July 2023 and still no job.

""" 
ACTIVITY

Create a shop dictionary, listing item as the key and the price as the value

Create a program which allows users to purchase from you store. Users should be able to input the item they want, and how many of them they wish to buy. 

Display a total cost from this information. 

Allow the user to keep purchasing items from your shop until they are done. Update the total as necessary
"""

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

name = input("\nPlease, tell us your name: ").capitalize()

# this function gets the time of the day and print the appropriate greeting for the current time
def greetings():
    if current_time >= 0 and current_time < 12:
        print (f"\nGood morning {name}. Welcome to Bruno Groceries.")
    elif current_time >= 12 and current_time < 18:
        print (f"\nGood afternoon {name}. Welcome to Bruno Groceries.")
    else:
        print (f"\nGood evening {name}. Welcome to Bruno Groceries.")

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
    while True: #this loop asks user what they want to buy. It repeats the question if user type something that's not in the shop inventory
        which_item = input("Please type the item you want to buy: ").capitalize()
        if which_item not in shop_inventory: 
            print(f"\nSorry {name}, we don't have {which_item} today. Please, try something from our inventory.")
            items_list()
        else:
            break
    while True: #this loop prevents user to type anything different than a number when they're asked how many of the previously typed product they want to buy
        try: 
            how_many = int(input(f"\nHow many {which_item}s would you like to buy {name}? "))
            break
        except:
            print(f"I'm sorry {name} but you have to type a number: ")
    #the if statement underneath add a product and quantity to the cart.
    if which_item in shop_cart:
        shop_cart[which_item] += how_many
    elif which_item not in shop_cart:
        shop_cart[which_item.capitalize()] = how_many  
    print("")
    print("ITEMS\t\tQTY\t\tTOTAL PRICE\n")
    overall_total = 0
    for key, value in shop_cart.items(): #loop that updates the overall total based on which_item user has chosen. Also does the math of how many items times the price for each one. 
        print(f"{key}\t\t{value}\t\t£{shop_inventory[key]*value:.2f}")
        overall_total += shop_inventory[key]*value
    print(f"\nOVERALL TOTAL: £{overall_total:.2f}")
    print("")

    still_shopping = input(f"Do you want to keep shopping {name}?\nType \"Y\" then ENTER to keep shopping or anything else to go for payment: ").capitalize()
    if still_shopping == "Y":
        items_list()
        continue
    else:
        break

#print the overall total with a thanks message to the customer
print(f"""
THE TOTAL FOR YOUR BASKET IS £{overall_total:.2f}.

Thank you for shopping with us, {name}.""")

#if statement that show a different goodbye message according to the hour of the day
if current_time >= 0 and current_time < 12:
        print ("\nHave a great day.\n")
elif current_time >= 12 and current_time < 18:
        print ("\nEnjoy your afternoon.\n")
else:
    print ("\nHave a good evening\n")


