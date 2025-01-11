""""
1. Alright, this is it. We are going to use all of our knowledge of functions to build out TripPlanner V1.0.

First, like in our previous exercises, we want to make sure to welcome our users to the application.

Create a function called trip_planner_welcome() that takes one parameter called name. The function should use print() to output a message like this:

"Welcome to tripplanner v1.0 <Name Here>"

Where <Name Here> represents the parameter variable of name we defined.

Call trip_planner_welcome(), passing your name as an argument.
"""

def trip_planner_welcome(name):
  return print(f"Welcome to tripplanner v1.0 {name}")

trip_planner_welcome("Bruno")

""""
2. Next, we are going to define a function called estimated_time_rounded() that will allow us to calculate a rounded time value based on a decimal for our user's trip.

An example call for this function will look like this:

estimated_time_rounded(2.5)

Where 2 represents 2 hours and .5 represents 30 minutes.

Define the function estimated_time_rounded() with a single parameter estimated_time. The function should do two things:

  1. Create a variable called rounded_time that is the result of calling the round() built-in function on the parameter estimated_time.
  2. Return rounded_time.

After the function definition, call estimated_time_rounded() with a decimal argument and save the result to a variable called estimate. Since this amount represents a time, be sure to use a positive number.
"""

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.5)

""""
3. Next, we are going to generate messages for a user's planned trip.

Create a function called destination_setup() that will have four parameters in this exact order:
  1. origin
  2. destination
  3. estimated_time
  4. mode_of_transport

Give the parameter mode_of_transport a default value of "Car". The program will error out if we run it since we have not defined a function body yet. Don't worry we will do that in the next step.
"""

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print(f"Your trip starts off in {origin}")
  print(f"And you are traveling to {destination}")
  print(f"You will be traveling by {mode_of_transport}")
  print(f"It will take approximately {str(estimated_time)} hours")
  
""""
4.
Next, we are going to write four print() statements in our function. The output on this function call should look like this:

Your trip starts off in <origin>
And you are traveling to <destination>
You will be traveling by <mode_of_transport>
It will take approximately <estimated_time> hours

Each of these print() statements use a different parameter from our function destination_setup().

Note: The estimated_time parameter will come in the form of an integer. Make sure to use str() to convert the parameter in your print statement.

After the function definition, call destination_setup() with the following arguments:
  - origin and destination should be string values representing the places you will travel from and to
  - Use the estimate you created earlier for estimated_time
  - If you will be traveling by a mode other than Car, be sure to overwrite the default value of mode_of_transport
"""

destination_setup("UK", "Brazil", estimated_time_rounded(10.6),"Plane")

""""
5. Great job! 👏

We have successfully finished our first version of the trip builder application. Go ahead and try passing different values into your functions!
"""

destination_setup("UK", "USA", estimated_time_rounded(8.7),"Airplane")