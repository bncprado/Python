printe = "hello world"
z = 0

print (f'\nThis is the "{printe}" exercise using "for loop":\n')
for number in range (13):
    z += 1
    print(f"{z}. {printe}")

z = 0

print (f'\nThis is the "{printe}" exercise using "while loop":\n')
x = 1
while x <= 13:
    x += 1
    z += 1
    print (f"{z}. {printe}")

print("")

"""Because we know how many times this process needs to occur, a for loop is the ideal choice. 
Well done for using range! Range creates a sequence for us, saving us the process of having to write out a list with 13 things in for us.

You've done a great job with the while loop - because we need a condition for it to run under, you've created yourself a counter to work with!

In both cases, you probably didn't need the z variable to show your result. 
I understand why you did it - but the number variable created in the for loop would work in that case, 
and you could either change your range to (1,14), or in the string you could say {number+1} 
to see the number you expected. Similar to that, in the while loop you could reference the x variable.

This isn't to say your way is wrong at all, and if the extra inclusions make things more understandable for you then to include them! Well done!"""





# fav_drinls=["coke", "beer", "bubble tea"]

# for i in fav_drinls:
#     print (i)

# answer=input("Who ordered a cortado? ")

# while answer != "Alex":
#     print ("incorrect")
#     answer=input("Type it again: ")

# print ("Enjoy your drink")