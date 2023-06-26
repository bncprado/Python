print("""

Create a variable called password.

Check how many letters are in the variable password. If there are fewer than 8, print that the password is too short.

Otherwise print the password.

""")

# if len(password) < 8:
#     print ("Password too short, please create a new one")
# else:
#     print (f"Your password is \"{password}\"")


while True:
    password = input ("\nPlease type your password: ")
    if len(password) < 8:
      print ("\nPassword too short, please create a new one. ")
    else:
      print (f"\nPassword accepted. Your password is \"{password}\"\n")
      break

    
  