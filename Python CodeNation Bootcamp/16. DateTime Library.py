import datetime

date_of_birth = datetime.datetime(1980,11,12)

today = datetime.datetime.now()

days = today - date_of_birth

print (f"\nBruno is alive for {days.days} days\n")

"""This is a very clear and efficient submission, 
making great use of lots of the things we've learnt so far.

The datetime library allows us to work with dates easily, 
and you've clearly done some great research into the methods available within it.

You've named your variables well, and with snake_case so they're extremely readable - 
I knew what each variable respresented!

You've given your answer clearly, in lots of context with the f string. This is great work!"""