import datetime


class BankAccount:
    def __init__(self, name, deposit, balance, pin):
        self.name = name
        self.initial_deposit = deposit
        self.balance = balance
        self.password = pin

    def password_check(self):
        while True:
            attempts = 0
            while True:
                user_pass = int(input("\nPlease type your password: "))
                if user_pass != self.password and attempts < 3:
                    attempts += 1
                    print(f"\nYou have {3 - attempts} more attempts")
                if user_pass != self.password and attempts == 3:
                    print("\nProgram will quit.")
                    quit()
                elif user_pass == self.password:
                    print(f"\nAccess granted, {self.name}.")
                    break
            break

    def deposit(self):
        # omg I finally found a way of executing a defined method inside a new method
        self.password_check()
        while True:
            try:
                figure = float(
                    input("\nPlease, type the amount you want to deposit: "))
                while figure <= 0:
                    print("\nPlease type a number bigger than 0")
                    figure = float(
                        input("\nPlease, type the amount you want to deposit: "))
                else:
                    self.balance = self.balance + figure
                    print(f"\nYour new balance is £{self.balance:.2f}")
                    break
            except:
                print("\nYou must type a number")

    def withdrawal(self):
        self.password_check()
        print(f"Your current balance is {self.balance}")
        while True:
            try:
                figure = float(
                    input("\nPlease, type the amount you want to withdraw: "))
                while figure <= 0:
                    print("\nPlease type a number bigger than 0")
                    figure = float(
                        input("\nPlease, type the amount you want to withdraw: "))
                else:
                    if self.balance - figure < 0:
                        print(
                            f"You don't have enough balance to withdraw £{figure:.2f}")
                        break
                    else:
                        self.balance = self.balance - figure
                        print(f"\nYour new balance is £{self.balance:.2f}")
                        break
            except:
                print("\nYou must type a number")

    def print_statement(self):
        print(f"\nYour current balance is £{self.balance:.2f}")
    
    def atm_operation(self):
        while True:
            print("""
PLEASE, SELECT THE OPERATION:
              
1. DEPOSIT      3. CHECK BALANCE
              
2. WITHDRAW     4. EXIT
              """)
            numbers = [1,2,3,4]
            while True:
                try:
                    operation = int(input("Please, type the number of operation and then ENTER to confirm: \n"))  
                    if operation not in numbers:
                        print("\nOnly numbers from 1 to 4 are valid options.\n")
                        continue
                    else:
                        break  
                except:
                    print("\nOnly numbers from 1 to 4 are valid options.\n")
            while True:
                if operation == 1:
                    self.deposit()
                    break
                elif operation == 2:
                    self.withdrawal()
                    break
                elif operation == 3:
                    self.print_statement()
                    break
                elif operation == 4:
                    print("Thanks for using Bruno Bank ATM Machines today.")
                    quit()
                elif operation not in numbers:
                    continue

    def atm_machine(self):
       # this variable gets current time of the day to be used in the greetings function
        current_time = datetime.datetime.now().time().hour

        # this function gets the time of the day and print the appropriate greeting for the current time
        def greetings():
            if current_time >= 0 and current_time < 12:
                print(f"\nGood morning {self.name}. Welcome to Bruno Bank.")
            elif current_time >= 12 and current_time < 18:
                print(f"\nGood afternoon {self.name}. Welcome to Bruno Bank.")
            else:
                print(f"\nGood evening {self.name}. Welcome to Bruno Bank.")
        greetings()
        self.atm_operation()
