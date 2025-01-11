""""
Nested functions provide a great example of how scope is determined in our program. Typically, the order of scope follows the pattern where inner functions are able to access outer function variables, but outer functions are not able to access inner function variables. Here is what that looks like in code:
"""

def outer_func():
    location = "Inside the outer function!"

    def inner_func():
        location = "Inside the inner function!"
        print(location)

    inner_func()

    print(location)

outer_func()

""""
In this example, we use location as the variable name for two local variables. Each instance of location has a different scope, so when the functions are called, Python uses the closest available scope for the variable definition. Because of this, when we call outer_func() we do not overwrite the value of location and both of the strings are printed.
"""