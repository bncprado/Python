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
                    print(f"\Hello again {self.name}.")
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
                    print("\nThanks for your visit. Have a great day")
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
                    figure = float(input("\nPlease, type the amount you want to withdraw: "))
                else:
                    if self.balance - figure < 0:
                        print(f"You don't have enough balance to withdraw £{figure:.2f}")
                        break
                    else:
                        self.balance = self.balance - figure
                        print(f"\nYour new balance is £{self.balance:.2f}")
                        break
            except:
                print("\nYou must type a number")

    def print_statement(self):
        print(f"\nYour balance is £{self.balance:.2f}")
