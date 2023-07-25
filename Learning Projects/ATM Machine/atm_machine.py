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
          user_pass = int(input("Please type your password: "))
          if user_pass != self.password and attempts < 3:
            attempts += 1
            print(f"You have {3 - attempts} more attempts")
          if user_pass != self.password and attempts == 3:
             print("Program will quit.")
             quit()
          elif user_pass == self.password:
            print(f"Welcome {self.name}.")
            break
        break

    def deposit(self):
      while True:
        try:
          figure = int(input("Please, type the amount you want to deposit: "))  
          self.balance = self.balance + figure
          break
        except:
          print("You must type a number")
      

        
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
      
      pass    

    def print_statement(self):
      print(f"Your balance is £{self.balance:.2f}")

        



