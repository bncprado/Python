""""
1. Our users want to be able to save a list of their favorite places in our travel application.

We have received a rough draft for this implementation from another coder, but there are some problems with variable scope which prevent it from working properly.

Take a second to understand what the program is doing and then hit Run the code to see the error.
"""

# This function will print a hardcoded count of how many locations we have.
favorite_locations = "Paris, Norway, Iceland" #this variable was inside the function "print_count_locations", making it impossible to the other function to access it. I've moved to outside the function, so the program can access it inside or outside the functions

def print_count_locations(): 
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()

""""
2. Looking at the error, it seems like the main issue is that favorite_locations is not defined. Why would our program not be able to see our beautiful favorite_locations variable?

Aha! It must be a scope issue. Fix the scope of favorite_locations so that both our functions can access it.
"""