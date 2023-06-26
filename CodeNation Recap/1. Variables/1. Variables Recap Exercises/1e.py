print("""

Create a variable called word that takes a string.

Create an if statement that checks if the last letter is the same as the first. If it is return true, otherwise return false.

""")
      
word = input("Please, type a word: ")

print("Are the first and last letter of the typed word the same? ")
if word.lower()[0] == word.lower()[-1]:
    print(True)
else:
    print(False)

