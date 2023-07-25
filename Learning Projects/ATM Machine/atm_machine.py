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
            print(f"\nWelcome {self.name}.")
            break
        break

    def check_if_number(self):
      pass

    def deposit(self):
      self.password_check() #omg I finally found a way of executing a defined method inside a new method
      while True:
        try:
          figure = float(input("\nPlease, type the amount you want to deposit: "))  
          while figure <= 0:
            print("\nPlease type a number bigger than 0")
            figure = float(input("\nPlease, type the amount you want to deposit: "))
          else:  
            self.balance = self.balance + figure
            print(f"Your current balance is {self.balance}")
            input("Deposit more? \n1. Yes\n2.No")
          break
        except:
          print("\nYou must type a number")
          
      

        
        # while True:
        #   if user_pass != self.password and attempts == 2:
        #     print("This is your last chance before program quits.")
        #     attempts += 1
        #     break
        #   elif user_pass != self.password:
        #     print("Wrong password.")
        #     attempts += 1
        #     print(attempts)
        #     break
        #   else: 
        #     figure = (input("Please, type the amount you want to deposit in numbers: "))
        #     if figure.isdigit():
        #         self.balance += float(figure)
        #         print(f"Your new balance is £{self.balance:.2f}")
        #     else:
        #         print("Deposit must be a number and greater than 0")
        # if attempts == 3:
        #     print("Password attempts exceeded. Program will quit")
        #     quit()          
            
    def withdrawal(self):
      self.password_check
      
      pass    

    def print_statement(self):
      print(f"Your balance is £{self.balance:.2f}")

        



