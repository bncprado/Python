"""
Write a small log-in program that asks a user to enter a password to continue. The user cannot continue until they get the password correct.

Add a limit to this program. Maybe the user can only try three times before they are locked out?

Remember your logical operators!
"""

password = input("\nPlease, type your password: ").lower()
attempt = 1

while password != "pass":
  if attempt == 3:
    print("\nToo many attempts. Program will quit\n")
    quit()
  elif attempt == 2:
    password = input("\nWRONG PASSWORD! This is your last chance, Type your password again: ")
  else: 
    password = input("\nWRONG PASSWORD! Please, type your password again: ")
  attempt += 1
else: 
  print("\nYou've logged in\n")

print("YOU GOT A STAR FOR ACCESSING THE PROGRAM\n")
  
