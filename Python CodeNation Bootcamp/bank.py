class BankAccount: #class that stores the bank account user details in different attributes like explained on each line:
    def __init__(self, first_name, deposit, balance, password):
        self.first_name = first_name #stores the first name of the user
        self.deposit = deposit #stores any deposit made when declaring the variable using the BankAccount object
        self.password = password #stores the user account password
        self.balance = balance #stores the current balance 
            
    def new_deposit(self,amount): #function used to make a new deposit to the current balance by adding the value the user inputs
        self.balance += amount
        print (f"\nYour current balance is {self.balance:.2f}") #it prints the balance after the deposit

    def withdrawal(self, amount): #function used to withdraw cash from the machine. It subtracts the typed value from the previous balance
        if self.balance - amount < 0: #if the requested amount by the user is larger than their current balance, the if statement prevents the machine to deliver the money, telling the user they don't have enough funds
            print ("\nSorry, you don't have enough funds to execute this operation")
            print (f"\nYour current balance is £{self.balance:.2f}") #shows the amount available in the account, giving the user a direction of how much they can withdraw
        else:
            self.balance -= amount
            print (f"\nYou've withdrawn £{amount:.2f}.\n\nYour current balance is £{self.balance:.2f}")#it prints the balance after the successfull withdraw

    def print_statement (self):#function that prints the balance
        print (f"\nYour current balance is {self.balance:.2f}")