"""
Previously, we wrote programs that only performed addition and subtraction. We can also perform multiplication and division in Python. To perform multiplication, we need to use the * character. For instance, to calculate the cost of purchasing Fruit Ninja Classic for two family members, we multiply 1.99 by 2:

print(1.99 * 2)
Output
3.98

To perform division, we use the / character. For example, to calculate splitting the cost Minecraft: Pocket Edition between three family members, we divide 6.99 by 3:

print(6.99 / 3)
Output
2.33

We can also perform exponentiation (raising a number to a power) by using **. For example, this is how we can raise 4 to the power of 2 (in mathematical notation, we'd write this as 
4
2
).

print(4 ** 2)

Output
16

The arithmetical operations we do in Python follow the usual order of operations from mathematics. Python calculates parentheses first, then exponentiation, then division and multiplication, and finally addition and subtraction. For example, knowing the order of operations is critical if we want to calculate the cost of purchasing 10 copies of Minecraft: Pocket Edition and 10 copies of Instagram:

print(6.99 + 0.00 * 10)
print((6.99 + 0.00) * 10)
Output
6.99
69.9

Looking at the code example above, we can deduce from the first operation (6.99 + 0.00 * 10) and its corresponding result (6.99), that multiplication precedes addition. This operation does not capture the cost of purchasing 10 copies of Minecraft: Pocket Edition!

However, for the second operation ((6.99 + 0.00) * 10), the addition is calculated first because this time it's surrounded by parentheses. Consequently, the result is 69.9.

So far, we've used space characters between numbers and operators (+, -, *, /, ** are operators). For instance, we've used 6.99 + 0.00 instead of 6.99+0.00. Both 6.99 + 0.00 and 6.99+0.00 will run correctly in Python; however, we encourage you to use spaces in your own code because it improves readability.

"""


"""
Write a program with three lines of code that performs the following arithmetical operations and displays the results (use the print() function to display the results):
"""
print(16*10)
print(48/5)
print(5**3)