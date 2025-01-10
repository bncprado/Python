#DEFINING A FUNCTION:
""""
1. Two of the most common NYC attractions include the Empire State Building and Times Square.

In travel.py, we'll write a function that prints the directions via subway from the Empire State Building to Times Square.

First, define a function, directions_to_timesSq(). Leave the body of the function empty for now.

Note: When we run the code, we will see an error: SyntaxError: unexpected EOF while parsing. This will occur when we don't populate a function with any statements. We will populate it with code in the next step.

EOF stands for “End of File” — Python is telling you that it was expecting some code in the body of the function, but it hit the end of the file first.
"""

def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")
  print("Take lots of pictures!")

""""
2. Within the body of the function, use three print() statements to output the following directions:

Walk 4 mins to 34th St Herald Square train station
Take the Northbound N, Q, R, or W train 1 stop
Get off the Times Square 42nd Street stop

Remember, if you run your code, you shouldn't see any output in the terminal at this point. Check out the hint if you want to see how to see the output (we will be doing it in the next section as well!)
"""

#CALLING A FUNCTION
""""
1. Call the directions_to_timesSq() function.

Click Run to see it execute and print out.
"""

directions_to_timesSq()

""""
2. Add an additional print statement to our directions_to_timesSq() function.

Have the statement print "Take lots of pictures!"

Run your code again and see how your output changes.
"""

#Whitespace & Execution Flow
""""
1. We are going to help our trip planner users figure out if they should travel today based on the weather. Let's let our users know we can check the weather for them.

Write a print() statement that will output Checking the weather for you!.
"""

print("Checking the weather for you!")


""""
2. We took a look outside and see a bright sunny day. Write a function called weather_check() that will print a message to our users that it's a great day to travel! The function should output: Looks great outside! Enjoy your trip.
"""

def weather_check():
  print("Looks great outside! Enjoy your trip.")
print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

""""
3. Oh no! It looks like some clouds came in and it started raining. Our users shouldn't go on a trip in the rain. In our weather_check() function add a second print() statement under the first one which prints a warning message for our travelers! It should print:

False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.
"""

"""
4. Call the function weather_check().
"""

weather_check()

""""
5. Unindent the final print statement (the one starting with “False Alarm”) in your weather_check() function. Run the program again.

What is different?
"""