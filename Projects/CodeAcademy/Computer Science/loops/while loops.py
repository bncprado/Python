"""
A while loop performs a set of instructions as long as a given condition is true.

The structure follows this pattern:

while <conditional statement>:
  <action>

"""

count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1

"""
Let's break the loop down:

1. count is initially defined with the value of 0. The conditional statement in the while loop is count <= 3, which is true at the initial iteration of the loop, so the loop body executes.

Inside the loop body, count is printed and then incremented by 1.

1. When the first iteration of the loop has finished, Python returns to the top of the loop and checks the conditional again. After the first iteration, count would be equal to 1 so the conditional still evaluates to True and so the loop continues.

2. This continues until the count variable becomes 4. At that point, when the conditional is tested it will no longer be True and the loop will stop.

The output would be:

0
1
2
3
"""

# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print(f"Count is currently {count}")
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# Your code below: 

countdown = 10
# while countdown >=0:
#   print(f"The number is still {countdown}")
#   countdown -= 1
# print("\nWe have liftoff!\n")

while countdown >=0:
  print(countdown)
  countdown -= 1