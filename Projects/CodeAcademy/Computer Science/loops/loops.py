ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])

print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")


"""
for <temporary variable> in <collection>:
  <action> (note the indentation)
"""

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

"""
Let’s break down each of these components:

1. A for keyword indicates the start of a for loop.
2. A <temporary variable> that is used to represent the value of the element in the collection the loop is currently on.
3. An in keyword separates the temporary variable from the collection used for iteration.
4. A <collection> to loop over. In our examples, we will be using a list.
5. An <action> to do anything on each iteration of the loop.

Let’s link these concepts back to our ingredients example. This for loop prints each ingredient in ingredients:
"""

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

for ingredient in ingredients:
  print(ingredient)

for sport in sport_games:
  print(sport)

#RANGE
"""

for <temporary variable> in <list of length 6>:
  print("Learning Loops!")

"""

six_steps = range(6)
# six_steps is now a collection with 6 elements:
# 0, 1, 2, 3, 4, 5

for temp in range(6):
  print("Learning Loops!")

print("")

for temp in range(6):
  print(f"Loop is on iteration number {temp+1}")

print("")

for temp in "a string":
  print(temp)

print("")

for temp in ["a","list"]:
  print(temp)

print("")

for temp in [["a", "list"],["of", "lists"]]:
  print(temp)