# """
# Functions allow us to break our code up into small, reusable chunks. When we need to use the function, we use its name.

# You've already been using them!

# print() len() input() lower() are all built-in functions!

# Someone else has already written the jobs those functions do, and we just use them when we need to!

# Note - a method like .lower() is a function that only works on a specific object

# """

# print("HELLO WORLD".lower()) # Some functions don’t need any specific information from us to work – they just do their job

# len() # Others might expect information from us to work with. It might have parameters. We fill in the spaces of the parameters with arguments.


# #--------------------------------------------------------------------------------------

# # This is the syntax used in Python when you're creating your own function

# def say_hello(): 

# # def is the keyword needed to let Python know you will be defining a new function. 

# # You name the function – paying attention to the naming convention. Functions should e well named for readability. Functions always end with () – even if we’re not giving it parameters.

# #Python is whitespace dependant. Anything that is indented after the : is part of that block, and will run when the function is called. In this example, the function will print the string “Hello”

#   print("Hello!")

# say_hello() # calling the function

# #--------------------------------------------------------------------------------------

# # Create a function to say goodbye. 

# def say_goodbye():
#   print("Goodbye!")

# say_goodbye()

# #--------------------------------------------------------------------------------------

# # PARAMETERS

# def say_something(something): # When we defined our function in this example, we also told it to expect some information. We told it how to work with this information without knowing exactly what it is, a bit like a variable! This is a parameter.
#     print(f"{something}")

# say_something("Hi bud") # When we call the function, we need to supply that instance of the function call with the information we want it to work with. This is an argument

# # This gives our function a lot more use cases! It’s more flexible, and can be used in many more situations.
# say_something("Hiya")
# say_something(3)
# say_something(True)

# #-------------------------------------------------------------------------------------

# # Think about a cash machine – it’s going to be doing the same jobs again and again, but with different data each time. Saving all this data as a new variable each time would be quite wasteful – parameters work better in this situation

# def cash_withdrawal(amount, accnum):
#     print(f"Withdrawing £{amount} from account {accnum}")

# cash_withdrawal(100, 50515253)
# cash_withdrawal(400, 55565758)
# cash_withdrawal(543, 60616263)

# #-------------------------------------------------------------------------------------

# """ 
# Create a function which takes a coffee order via two parameters: size and type_of_drink. Print them in a sentence 

# """
# def coffee_order(size, type_of_drink):
#     print(f"You've ordered a {size} {type_of_drink}")

# coffee_order("large", "machiatto expresso caravaggio nicaragua fish and chips tea")
# coffee_order(750, "carbonatto fibonatto machiato")

# #-------------------------------------------------------------------------------------

# # DIGGING DEEPER - SCOPE

# """ 
# Variable scope refers to the region of the code where we can access variables. We'll be looking at the two main Python scopes - GLOBAL and LOCAL
# """ 

# balance = 1000 # balance is in the global scope – the whole program can access the name balance, and see the data inside.

# def cash_withdrawal(amount, accnum): # Functions are local scoped. What happens in the function call stays in the function call. If we tried to access amount or accnum outside of the function, we would get an error.
#     print(f"You have {balance} in your account")
#     print(f"You are withdrawing {amount} from {accnum}")
#     balance -= amount #this will not work cause Python is treating the balance variable inside as a local scope. That means it can't change the global variable balance cause, despite having access to it, it's not able to change it

# #-------------------------------------------------------------------------------------

balance = 1000 

def cash_withdrawal(amount, accnum): 
    global balance #this line is telling python we want to access the global variable "balance" outside the function and modify it 
    print(f"You have {balance} in your account")
    print(f"You are withdrawing {amount} from {accnum}")
    balance -= amount # this line of code will update the global variable balance and it'll be reflected globally
    print(f"Your updated balance is {balance}")
  
cash_withdrawal(200, 12345678)






    

