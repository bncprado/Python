print("""

Create a variable called word that takes a string.

Create an if statement that checks if the whole string is a palindrome (reads the same forwards as it does backwards e.g. abba)

""")
      
word = input("\nPlease, type a word: ".lower())

print("Is the word a palindrome (reads the same forwards as it does backwards)?")
if word == word[::-1]:
    print(f"\n{True}, the word \"{word}\" is a palindrome")
else:
    print(f"\n{False}, the word \"{word}\" is NOT a palindrome")
    
