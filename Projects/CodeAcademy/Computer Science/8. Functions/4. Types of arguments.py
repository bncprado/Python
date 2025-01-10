""""
1. Tripcademy (our trusty travel app) needs to allow passengers to plan a trip (duh).

Write a function called trip_planner() that will have three parameters: first_destination, second_destination and final_destination.

Give the final_destination parameter a default value of "Codecademy HQ".

Note: Since we did not define any code in our function yet, we will receive an error in our output terminal. Don't worry, we will be filling in the code in the next step.
"""

def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print(f"First, we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}")

""""
2. First, we want to introduce the trip to users. Use print() in our function to output "Here is what your trip will look like!".
"""

""""
3. In our function definition let's provide an itinerary that will describe the destinations our user will visit in order. Print a statement that follows this form:

First, we will stop in <first_destination>, then <second_destination>, and lastly <final_destination>

An example call to our function using positional arguments:

trip_planner("London", "India", "New Zealand")

Should output:

Here is what your trip will look like!
First, we will stop in London, then India, and lastly New Zealand

To test out your function, call trip_planner() with the following values for the parameters:

first_destination: "France"

second_destination: "Germany"

final_destination: "Denmark"
"""

trip_planner("France", "Germany", "Denmark")

""""
4. Call the function trip_planner() again with the following values for the parameters:

first_destination: "Denmark"

second_destination: "France"

final_destination: "Germany"

Note the difference in your output depending on the position of your arguments.
"""

trip_planner("Denmark", "France", "Germany")

""""
5. Call the function trip_planner() again but this time include the keyword arguments (e.g. first_destination) and put them in this exact order:

first_destination = "Iceland"

final_destination = "Germany"

second_destination = "India"
"""

trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")

""""
6. Lastly, go ahead and call the function trip_planner() using only two positional arguments to see the default argument in action:

first_destination: "Brooklyn"

second_destination: "Queens"
"""

trip_planner("Brooklyn", "Queens")