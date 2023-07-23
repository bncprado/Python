shop_inventory = { #shows the items available in the shop
    "Coke" : 0.55,
    "Bread" : 1.29,
    "Ham" : 2.00,
    "Cheese" : 3.25,
    "Peanut" : 2.49 
}

print("\nWelcome to Bruno's Groceries Shop!")

def show_inventory():
    print("\nThese are the items available today:\n\nITEMS\t\tPRICE\n")
    for i, y in shop_inventory.items():
        print(f"{i}\t\t£{y:.2f}")
    print("")

coke_total_price = 0
coke_total_items = 0

# def buy():
while True:
    show_inventory()
    which_item = (input("Type the item you want to buy: ").lower())
    if which_item == "coke":
        how_many = (int(input(f"\nType how many {which_item} you'd like to buy: ")))
        result = (how_many * shop_inventory.get("Coke"))
        print (f"\nThe total for {how_many} Cokes is £{result:.2f}")
        coke_total_items += how_many
        anything_else = input("Would you like to buy anything else? Y or N: ").lower()
        while True: 
            if anything_else == "n":
                break
            else: 
                continue
                
# buy()

# buy_another = input("\nWould you like to buy another item? Type Y or N, please: ".lower())

# if buy_another == "y":
#     buy()
# else:
#     print("Thank you for shopping with us")

        

# print (f"£{coke_price:.2f}")









# store_inventory = {"Apple ".strip(): 1.00, 
#                    "Banana": 1.00, 
#                    "Bread ".strip(): 1.50, 
#                    "Cake  ".strip(): 3.00, 
#                    "Cola  ".strip(): 2.00, 
#                    }

# def print_inventory():
#     print('')
#     for i, j in store_inventory.items():
#         print(f"{i} \t£{j:.2f}")

# still_shopping = True
# total = 0
# order_number = 1
# book_of_orders = []

# # Main Game Loop
# print("\nWelcome to our store! Here is our inventory\n")
# while still_shopping:
#     print_inventory()
#     # Check the user inputs correct 
#     while True: 
#         user_choice = input("\nWhat would you like to order?:  ").capitalize()
#         if user_choice in store_inventory.keys():
#             break
#         print("\nThat item is not in the inventory\n")
#     while True:
#         try:
#             quantity = int(input(f"\nHow many {user_choice.lower()}s would you like to buy?:  "))
#             current_total = quantity * store_inventory.get(user_choice.capitalize()) 
#             total += current_total
#             book_of_orders.append({"order_number":order_number,
#                                     "quantity": quantity,
#                                     "price": store_inventory[user_choice.capitalize()],
#                                    "item": user_choice.capitalize(), 
#                                     "total": current_total, 
#                                      "overall_total": total,  })
#             order_number += 1
#             print(f"\nYou have added {quantity} {user_choice.lower()}s to your basket\n")
            
#             print(f"""
# \tItem\t|\tPrice\t|\tQty\t|\tTotal\t
# ----------------------------------------------------------------------
#     """, end="")
#             for i in book_of_orders:
#                 print(f"""\t{i["item"]}\t\t£{i["price"]:.2f}\t\t{i["quantity"]}\t\t£{i["total"]:.2f}""")
#             print(f"""\nOverall Total: £{i["overall_total"]:.2f}""")
#             break
#         except ValueError:
#             print("\nThat is not a number. Please enter a valid number\n")
#     while True:
#         quit = input("\nWould you like to add more items to your basket? ( Y | N ) ")
#         if quit.upper() == "Y":
#             break
#         if quit.upper() == "N":
#             while True:
#                 sure = input("\nAre you sure? ( Y | N ) ")
#                 if sure.upper() == "Y":
#                     still_shopping = False
#                     break
#                 elif sure.upper() == "N":
#                     break
#             break
#     if not still_shopping:
#         print(f"\nYour total is £{total:.2f}\n")
#         print("Thank you for shopping with us. We hope to see you again soon.")



    

    




