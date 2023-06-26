print("""

Correct the code on the following slide so it functions as expected.

Can you use anything to make sure “London” and “london” are accepted as correct answers?

CODE:
print ("What is the capital of England?")

answer = input(Type your answer>> )

if answer="London"
  print("Correct! The answer is {answer}")
Else:
  prnt("Incorrect, the answer is London, not {answer}")

""")
      
answer = input("Type your answer: ")

if answer == "London".lower():
  print(f"Correct! The answer is {answer.capitalize()}")
else:
  print(f"Incorrect, the answer is London, not {answer.capitalize()}")

