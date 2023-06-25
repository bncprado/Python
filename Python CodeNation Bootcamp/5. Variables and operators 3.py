apple_price = 0.25

numberOfApples = int(input("\nPlease, type how many apples you'd like to buy > "))

print("")

if  numberOfApples <4:
    print (f"The total price for {numberOfApples} apples is {numberOfApples*apple_price*100:.0f}P\n")
else:
    print (f"The total price for {numberOfApples} apples is £{numberOfApples*apple_price:.2f}\n")
