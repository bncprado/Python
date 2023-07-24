"""
ACTIVITY

Using objects, create a bank account.

Include the attributes; name, deposit, and balance

Include the methods: deposit, withdrawal, print statement.

Create an atm machine

Ensure the user enters the correct pin, and do not allow a withdrawal if there are insufficient funds.

"""

from atm_machine import BankAccount

acc1 = BankAccount("Bruno", 0, 0, 0000)
acc1.deposit("bruno")
acc1.print_statement()