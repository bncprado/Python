print("""

Create 5 lists. Each list will contain 6 words.

Create a program which allows a user to pick a word from each list by choosing a number. The user shouldn’t see the lists before they chose.

Fill in the blanks of this poem using the randomly selected words:

"Twas {word1}, and the {word2} toves Did gyre and {word3} in the wabe:

All {word4} were the borogoves, And the {word5} raths outgrabe. "

""")

list1 = ['', 'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
list2 = ['', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine']
list3 = ['', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine']
list4 = ['', 'watermelon', 'blueberry', 'blackberry', 'pineapple', 'pomegranate', 'guava']
list5 = ['', 'apricot', 'coconut', 'mulberry', 'lime', 'plum', 'passionfruit']

word1 = int(input("""

You'll be asked to type a number from 1 to 6 five times. 

For each time, you'll be choosing a random word from a list to fill the following poem:

"Twas {word1}, and the {word2} toves Did gyre and {word3} in the wabe:

All {word4} were the borogoves, And the {word5} raths outgrabe.""

Please, type a number from 1 to 6 for word1: """))

word2 = int(input("Now, type a number from 1 to 6 for word2: "))
word3 = int(input("Now, type a number from 1 to 6 for word3: "))
word4 = int(input("Now, type a number from 1 to 6 for word4: "))
word5 = int(input("And finally, type a number from 1 to 6 for word5: "))

print(f"""
"Twas {list1[word1]}, and the {list2[word2]} toves Did gyre and {list3[word3]} in the wabe:

All {list4[word4]} were the borogoves, And the {list5[word5]} raths outgrabe."      

""")

