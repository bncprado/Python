"""adding new key and values to an empty dict and updating the values after creating it""" 
shop_list = {}



while True:
    which_item = input("Which item? ").capitalize()
    how_many = int(input("How many? "))
    if which_item in shop_list:
        shop_list[which_item] += how_many
    elif which_item not in shop_list:
        shop_list[which_item.capitalize()] = how_many
    print(shop_list)
    x = input("Do you want to continue? Type \"Y\" for yes or anything else to quit: ").capitalize()
    if x == "Y":
        continue
    else:
        break
    

print(shop_list)
