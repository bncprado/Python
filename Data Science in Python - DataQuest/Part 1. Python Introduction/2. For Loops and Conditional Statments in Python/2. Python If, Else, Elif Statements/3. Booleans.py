"""
Previously, we used if price == 0.0 to check whether price equals 0.0. When we use the == operator to determine if two values are equal, the output will always be True or False:

print(4 == 4) # This is true
print(4 == 7) # This is false

Output
True
False

Here's another example:

price = 0

print(price == 0)
print(price == 2)

Output
True
False

Although they may look like strings, True and False belong to a different data type:

print(type(True))

Output
<class 'bool'>

print(type(False))

Output
<class 'bool'>

We call True and False Boolean values or Booleans — we can see in the code example above that their data type is bool ("bool" is an abbreviation for "Boolean").

Instructions

In the code editor, we've already initialized the variable a_price with a value of 1. Transcribe the following sentences into code:

  1. Print a_price equals 0.
  2. Print a_price equals 1.

Do not modify the a_price variable.

GIVEN CODE

a_price = 1

"""

a_price = 1
print(a_price == 0)
print(a_price == 1)