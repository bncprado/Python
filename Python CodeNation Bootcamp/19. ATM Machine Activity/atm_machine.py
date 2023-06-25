from bank import BankAccount

def anything_else (): #defines the function that asks the user if they wanna do anything else after already done something, or simply quit
        print ("\nWould you like to do anything else? If not, type \"4\" to quit.")

account_n1 = BankAccount("Bruno", 0, 1000, 1234) #variable that stores the object created based on the class BankAccount

print (f"\nHi {account_n1.first_name}. Welcome to your exclusive ATM machine.") #greeting message using the object attribute first_name.

password_check = int(input("\nPlease, type your password: ")) #variable that will ask the user to type the password

while True: #while true statement that verifies if the typed password matches with the password in the mentioned object
    if password_check == account_n1.password:
        print ("\nAccess granted.")
        break 
    else:
        print ("\nWrong password, try again")
        password_check = int(input("\nPlease, type your password: "))

print ("\nWhat would you like to do today?")

atm_options = ["", "Deposit", "Withdrawal", "Statement", "Quit"] #list that stores the functionalities available at the machine. Note that the indexed position 0 was filled with an empty string. This is because I didn't want to confuse the user by tiping 0 to choose something

while True: #while statement that has most of the functionalities of the ATM machinew
    atm_selection = int(input("""
1. Deposit
2. Withdrawal
3. Statement
4. Quit

Please, select by choosing a number: """)) #variable that asks the user to input the number related to the desired function

    if atm_selection == 3: #part of the if statement that executes the code if the user selects option 3. statement
        account_n1.print_statement() #object of the class BankStatement using the method defined to print the statement
        anything_else()

    elif atm_selection == 2:#part of the if statement that executes the code if the user selects option 2. withdrawal
        account_n1.withdrawal(int(input("\nType the amount you'd like to withdraw: ")))#object of the class BankStatement using the method defined to withdraw from the balance and update the value of the balance
        anything_else()

    elif atm_selection == 1:#part of the if statement that executes the code if the user selects option 1. deposit
        account_n1.new_deposit(int(input("\nType the amount you'd like to deposit: ")))#object of the class BankStatement using the method defined to deposit into the balance and update the value of the balance
        anything_else()
        
    elif atm_selection == 4:#part of the if statement that executes the code if the user selects option 4. quit that sends a goodbye message and close the program
        print ("\nHave a nice day :)\n")
        break    
    elif atm_selection != 1 or 2 or 3 or 4:#part of the if statement tells the user to not type anything different than 1,2,3 or 4
        print ("\nPlease, select only numbers from 1 to 4")
