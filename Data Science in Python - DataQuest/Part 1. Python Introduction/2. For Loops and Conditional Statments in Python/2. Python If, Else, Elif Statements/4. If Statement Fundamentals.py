"""

Boolean values (True and False) are necessary parts of any if statement. One of the following must always follow if: (1) a Boolean value, or (2) an expression that evaluates to a Boolean value. Below, a boolean value follows if:

if True:
    print(100)

Output
100

In the following code, 1 == 1 evaluates to True:

if 1 == 1:
    print(100)

print(1 == 1)

Output
100
True

We should indent the code in the body of an if statement four spaces to the right (technically, we only need to indent the code one space to the right, but the convention in the Python community is to use four spaces per indentation level — this is an important habit to form in case you collaborate with others).

if True: 
    print(1) # body

Output
1

if True: 
print(1)

Output
IndentationError: expected an indented block

The indented code only executes when True follows if. When False follows if, the code inside the body doesn't execute. Notice in the diagram below that 'First Output' and 'Third Output' are printed, while 'Second Output' isn't.

if True:
    print('First Output')

if False:
    print('Second Output')

if True:
    print('Third Output')

Output
First Output
Third Output

Note that we can have more than one line of code in the body of an if statement. Below, we see three lines of code for each if statement.

if False:
    print('A')
    print('B')
    print('C')

if True:
    print(1)
    print(2)
    print(3)

Output
1
2
3

Instructions

In the code editor, we've provided three pairs of statements for use in this exercise. Recall that the indented code only executes when True follows if. When False follows if, the code inside the body doesn't execute. Let's leverage this behavior to only print the statements where both statements are true.

  1. Review the pairs of statements provided in the code editor.
  2. Correct the boolean following the if statement when one or both statements are false, so that the code inside the body doesn't execute.
    - We only want to print statements where both statements are true.
    
GIVEN CODE:

if True:
    print("2 + 2 == 5")
    print("lemons are sour")

if True:
    print("the sky is blue")
    print("5 >= 3")
    
if True:
    print("spheres have corners")
    print("7 / 5 == 2")

EXPECTED OUTPUT:

the sky is blue
5 >= 3

"""

if False:
    print("2 + 2 == 5")
    print("lemons are sour")

if True:
    print("the sky is blue")
    print("5 >= 3")
    
if False:
    print("spheres have corners")
    print("7 / 5 == 2")