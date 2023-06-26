print("""

Create a variable called "num".

Check if the variable is divisible by 3 or 5. If yes, print “This number is divisible by 3 or 5” to the terminal.

Otherwise print “This number is not divisible by 3 or 5”.

""")

num = int(input("Please, type a number to check if it's divisible by 3 or 5: "))

if num%5 == 0 or num%3 == 0:
    print("\nThis number is divisible by 3 or 5")
else:
    print("\nThis number is not divisible by 3 or 5")

