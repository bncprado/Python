from colorama import Fore, init
init(autoreset=True) #it doesn't work properly, or I'm doing something wrong and didn't notice
#ADDED COLOUR TO BETTER SEE THE TEXTS

#addition .It adds the typed numbers in the code

print (Fore.YELLOW + """ 
 ----------------------
| ARITHMETIC OPERATORS |
 ----------------------
 """)

print (f"""This is the {Fore.YELLOW}ADDITION{Fore.RESET} example.

Type the numbers to ADD them.
""")
#this version has a simplified print statement above

addnum1 = int(input(Fore.GREEN + "Please type number 1: "))
addnum2 = int(input("Please type number 2: "))
# this line of code is not necessary anymore -> addresult = addnum1 + addnum2

print(Fore.BLUE+  f"\nThe result is: {addnum1+addnum2}".upper())

print ("\n---------------------------------------------------------------------------")

#subtraction. It subtracts the typed numbers in the code

print(f"""
This is the {Fore.YELLOW}SUBTRACTION{Fore.RESET} example.

Type the numbers to SUBTRACT them.
""")

subtnum1 = int(input(Fore.GREEN + "Please type number 1: "))
subtnum2 = int(input("Please type number 2: "))


# this line of code is not necessary anymore -> subtresult = subtnum1 - subtnum2

print(Fore.BLUE+  f"\nThe result is: {subtnum1-subtnum2}".upper())#MORE ATTENTION WITH THE OPERATORS

print ("\n---------------------------------------------------------------------------")

#Multiplication. It multiplies the typed numbers in the code

print(f"""
This is the {Fore.YELLOW}MULTIPLICATION{Fore.RESET} example.

Type the numbers to MULTIPLY them.
""")
multnum1 = int(input(Fore.GREEN + "Please type number 1: "))
multnum2 = int(input("Please type number 2: "))

# this line of code is not necessary anymore -> multresult = multnum1 * multnum2

print(Fore.BLUE+  f"\nThe result is: {multnum1*multnum2}".upper())

print ("---------------------------------------------------------------------------")

#Exponential. It multiplies the typed numbers exponentialy in the code
print(f"""
This is the {Fore.YELLOW}EXPONENTIAL{Fore.RESET} example.

Type the numbers to EXPONENTIALY them.
""")

expnum1 = int(input(Fore.GREEN + "Please type number 1: "))
expnum2 = int(input("Please type number 2: "))

# this line of code is not necessary anymore -> expresult = expnum1 ** expnum2

print(Fore.BLUE+  f"\nThe result is: {expnum1**expnum2}".upper())

print ("---------------------------------------------------------------------------")

#Division. It divides the typed numbers in the code

print(f"""
This is the {Fore.YELLOW}DIVISION{Fore.RESET} example.

Type the numbers to DIVIDE them.
""")

divnum1 = int(input(Fore.GREEN + "Please type number 1: "))
divnum2 = int(input("Please type number 2: "))

# this line of code is not necessary anymore -> divresult = divnum1 / divnum2

print(Fore.BLUE+  f"\nThe result is: {divnum1/divnum2}".upper())

print ("---------------------------------------------------------------------------")

#Modulo (remainder). It divides the numbers using only integers and shows ONLY what lasts of that division.
#for an instance 10/3 = 3 and 1 is the remainder. So it will show number 1

print(f"""
This is the {Fore.YELLOW}REMAINDER{Fore.RESET} example.

Type the numbers to show the REMAINDER of the division.
""")
      
modnum1 = int(input(Fore.GREEN + "Please type number 1: "))
modnum2 = int(input("Please type number 2: "))

# this line of code is not necessary anymore -> modresult = modnum1 % modnum2
print(Fore.BLUE+  f"\nThe result is: {modnum1%modnum2}".upper())

print ("---------------------------------------------------------------------------")