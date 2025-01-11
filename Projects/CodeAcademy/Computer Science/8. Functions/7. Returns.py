""""
1. Our travel application is getting really popular. Some of our users have posted on social media that it would be useful if our application could help them track their budget during trips. We want to help them track their starting budget and let them know how much they have left after an expense.

We have provided some starting code to get started. Take a second to understand the code and then click Run and take a look at the output.
"""

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 

""""
2. Let's create a new function called deduct_expense() that will take two parameters.

The first parameter will be budget and the second parameter will be expense. Our function will be taking in a budget value as well as the expense we want to subtract.

We will want our function to return the budget minus the expense our travelers are incurring.
"""
shirt_expense = 9

new_budget_after_shirt = None 

def deduct_expense(budget, expense):
  return budget-expense


""""
3. Looks like the most common expense our travelers are incurring is a t-shirt purchase.

Let's create a variable called shirt_expense and for now, we will give it a set value of 9 (We are not accounting for currency changes at the moment). Make sure this is defined outside of the functions in your script.
"""

""""
4. Now that we have an expense to subtract, create a new variable called new_budget_after_shirt and set it to be the function call of deduct_expense().

Pass our current_budget variable as the first argument and the shirt_expense variable as the second argument.
"""

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

""""
5. Lastly, we want our users to see the remaining budget.

Call the provided print_remaining_budget() function, passing in new_budget_after_shirt as the only argument.
"""

print_remaining_budget(new_budget_after_shirt)

""""
6. Great Job! This is the biggest program with functions we have built so far! Take a second to review your code and click Run one last time when you are ready to move on.
"""