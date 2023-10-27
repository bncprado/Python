"""
Write a small log-in program that asks a user to enter a password to continue. The user cannot continue until they get the password correct.

"""

password = input("\nPlease, type your password: ")
while password != "pass":
    print("\nWrong password, please type it again")
    password = input("\nPlease, type your password: ")
else:
    print("\nYou have logged in")