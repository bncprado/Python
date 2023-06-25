# password = input("\nType your password: ")

# x = 0

# while password != "password" and x < 2:
#     password = input("\nWRONG, type it again: ")
#     x += 1
# if password != "password":
#     print ("\nACCESS DENIED. Too many attempts.\n")
# else: 
#     print ("\nACCESS GRANTED.\n")

"""This is an excellent submission! You've written a very specific condition for the while loop to run under - 
while the password is wrong AND they still have enough chances to try again. This is very clear. 
I would always recommend you do this over a while True loop, well done!



You've also correctly identified that there will be two situations that will break the loop - 
the password being right, or them running out of chances. 
You've handled these very well with your if statement nested within the else of the loop. 
I've tested this a few times, and it seems to work really well.

My only comment is your "x" variable - functionally this makes no difference, 
but for readability I would suggest giving it a clearer name like "attempts".

Well done!"""
x=0
while True:
    x+=1
    prompt = input ("Type your password: ")
    if prompt != "password" and x!=3:
        print ("\nPassword's not right\n")
    else: 
        print ("\nAccess granted\n")
        break