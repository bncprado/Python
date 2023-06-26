print("""

A shop sells apples for 25p per apple.

Create a program which asks a user how many apples they want to buy.

Display the total cost of the apples in both pence, and pounds and pence.

""")
apple_price = 25      
how_many = int(input('Type the number of apples you\'d like to buy: '))
final_price = how_many * apple_price

if final_price < 100:
    print (f'\nThe total cost for {how_many} apples is {final_price}P')
else:
    print (f'\nThe total cost for {how_many} apples is £{final_price/100:.2f}\n')






