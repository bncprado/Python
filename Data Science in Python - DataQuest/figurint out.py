"""how to multiply values using the key of a dictionary"""

shop_list = {}


def question():
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
    
question()

print(shop_list)
