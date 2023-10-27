import time
from datetime import date

print("""
Activity 1
Create a program which calculates how many days you've been alive for.
HINTS - look into the datetime library, and don't use input!
""")

day_i_was_born = date(1980,11,12)
today = date.fromtimestamp(time.time())
days_alive = today - day_i_was_born

print(f"I've been alive for {days_alive.days} days")


