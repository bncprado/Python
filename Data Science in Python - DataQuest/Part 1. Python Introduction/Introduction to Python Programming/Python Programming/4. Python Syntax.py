"""
Previously, we sent the computer two instructions and wrote each on a separate line. If we were to put them both on the same line, we'd get an error:

print(0.00 + 6.99) print(4.5 - 3.5)
Output
    print(0.00 + 6.99) print(4.5 - 3.5)
                        ^
SyntaxError: invalid syntax

print(0.00 + 6.99) print(4.5 - 3.5) resulted in text describing a syntax error. This is because all programming languages — Python included — have syntax rules. Each line of instructions has to comply with these rules.

This is similar to the syntax rules we follow in verbal languages. If you want to tell a friend that you like data science in English, you need to follow the syntax rules to correctly convey your message. Your friend will understand "I like data science," but not "science I data like." Similarly, the computer didn't understand two print() statements on one line because the syntax was incorrect.

Running into errors is common when we're programming, and we'll constantly learn about errors and how to fix them. Now let's practice giving the computer more instructions by printing some information about the app Clash of Clans.

track_name                  price	  currency	  rating_count_tot	  user_rating
Facebook	                  0.0	    USD	        2974676	            3.5
Instagram	                  0.0	    USD	        2161558	            4.5
Clash of Clans	            0.0	    USD	        2130805	            4.5
Fruit Ninja Classic	        1.99	  USD	        698516	            4.5
Minecraft: Pocket Edition	  6.99	  USD	        522012	            4.5
"""

"""
Instructions

Fix the code. 

Remember that each instruction must be on a separate line.

print(0.00) print(2130805) print(4.5)

"""
print(0.00) 
print(2130805) 
print(4.5)