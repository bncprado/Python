""""
1. We want to create a program that allows our users to generate the directions for their upcoming trip!

Create a function called generate_trip_instructions() that defines one parameter called location.

Note: Since we did not define any code in our function yet, we will receive an error in our output terminal. Don't worry, we will be filling in the code in the next step.
"""

def generate_trip_instructions(location):
  print(f"Looks like you are planning a trip to visit {location}")
  print(f"You can use the public subway system to get to {location}")

""""
2. generate_trip_instructions() should print out the following:

Looks like you are planning a trip to visit <location>


Where <location> will represent the location parameter.
"""

""""
3.generate_trip_instructions() should also let our users know they can reach their location using public transit.

Let's have generate_trip_instructions()also print out the following on a new line:

You can use the public subway system to get to <location>

Where <location> will represent the location parameter.
"""

""""
4. Time for some greenery! Let's see what happens when we call the function and input the argument "Central Park", a backyard wonder in the heart of New York City.
"""
generate_trip_instructions("Central Park")

"""
5.
The day trip is over and we need to get back to the train station to head home. Change the argument to "Grand Central Station" and call the function again.

What changed in the output?
"""

generate_trip_instructions("Grande Central Station")