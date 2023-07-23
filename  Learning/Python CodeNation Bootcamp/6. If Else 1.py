#this was an exercise based on if statements only. But I've created a while true loop to give a more realistic input and result
from colorama import Fore, init
#init(autoreset=True)
password_attempts=0

while True:
    print(Fore.LIGHTYELLOW_EX+"")
    password_attempts+=1
    password = input("\nPlease, create a password with at least 8 characters: ")
        
    if len(password) < 8:
        print (f"\nYour password is too short. Please, run the code again and retype a new password with at least 8 characters")    
        if password_attempts == 2:
            print(Fore.RED + "\nTHIS IS YOUR LAST CHANCE, PROGRAM WILL QUIT AFTER 3rd MISTAKE")
        elif password_attempts == 3:
            print (Fore.RED + "\nTOO MANY ATTEMPTS, PROGRAM WILL QUIT\n")
            quit()
    else: 
        print (f"\nYour new password is \"{password}\" \n")
        break
