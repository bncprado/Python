class BankAccount:
    def __init__(self, name, deposit, balance, pin):
        self.name = name
        self.initial_deposit = deposit
        self.balance = balance
        self.password = pin

    def deposit(self):
      while True:
        user_pass = int(input("Please type your password: "))
        attempts = 0
        
        if user_pass != self.password and attempts == 3:
            print("Password attempts exceeded. Program will quit")
            quit()
          
        elif user_pass != self.password and attempts == 2:
          print("This is your last chance before program quits.")
          attempts += 1
          
        elif user_pass != self.password:
          attempts += 1
          print("Wrong password.")
          
        else: 
          figure = (input("Please, type the amount you want to deposit in numbers: "))
          if figure.isdigit():
              self.balance += float(figure)
              print(f"Your new balance is £{self.balance:.2f}")
              break
          else:
              print("Deposit must be a number and greater than 0")
                
            
def withdrawal(self):
  pass    

def print_statement(self):
    print(f"Your balance is £{self.balance:.2f}")

        



