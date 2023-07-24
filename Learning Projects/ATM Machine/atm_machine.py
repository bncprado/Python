class BankAccount:
    def __init__(self, name, deposit, balance, pin):
        self.name = name
        self.initial_deposit = deposit
        self.balance = balance
        self.password = pin

    def deposit(self, i):
        while True:
            try: 
              self.balance += float(i)
              break
            except:
              print("Please, use numbers only")
                
    def withdrawal(self, i):
        self.balance -= i
    
    def print_statement(self):
        print(f"£{self.balance:.2f}")

        
   
    


