shop_list = {}

shop_inventory = {
    'Apple': 0.99,
    'Banana': 0.5,
    'Orange': 0.75,
    'Milk': 2.49,
    'Bread': 1.99,
}

while True:
    while True:
        which_item = input("\nWhich item? ").capitalize()
        if which_item not in shop_inventory:
            print("Please, choose something that is in our inventory")
        else:
            break
    how_many = int(input("\nHow many? "))
    if which_item in shop_list:
        shop_list[which_item] += how_many
    elif which_item not in shop_list:
        shop_list[which_item.capitalize()] = how_many  
    print("")
    print("ITEMS\t\tQTY\t\tTOTAL PRICE\n")
    overall_total = 0
    for key, value in shop_list.items():
        print(f"{key}\t\t{value}\t\t£{shop_inventory[key]*value:.2f}")
        overall_total += shop_inventory[key]*value
    print(f"\nOVERALL TOTAL: £{overall_total:.2f}")
    print("")

    x = input("Do you want to continue? Type \"Y\" for yes or anything else to quit: ").capitalize()
    if x == "Y":
        continue
    else:
        break
    

print(shop_list)
