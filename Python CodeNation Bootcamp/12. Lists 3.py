list_1 = [
    None, #can be "None" or just a pair of double quotes to fill the 0 position
    "tomato",
    "banana",
    "apple",
    "carrot",
    "orange",
    "grape"
]

list_2 = [
    "",
    "golf",
    "polo",
    "passat",
    "corsa",
    "zafira",
    "c4"
]

list_3 = [
    "",
    "São Paulo",
    "New York",
    "London",
    "Tokyo",
    "Buenos Aires",
    "Lisbon"
]

list_4 = [
    "",
    "Brazil",
    "United Kingdom",
    "India",
    "South Africa",
    "Japan",
    "Australia"
]

list_5 = [
    "",
    "Facebook",
    "Amazon",
    "Google",
    "Microsoft",
    "Apple",
    "Samsung"
]

print ("\nThe following poem has some words missing. The missing words are represented by the brackets:\n")
print ('"Twas (), and the () toves Did gyre and () in the wabe:\nAll () were the borogoves,\nAnd the () raths outgrabe."\n')
print ('We will get 5 random words to fill the brackets.\nYou have to type from 1 to 6 to get a random word for each bracket.\n"1" will represent the first word and "6" the last word of a "secret list".')

word1 = list_1[int(input("\nType from 1 to 6 to get a word from secret list 1: "))]
word2 = list_2[int(input("Type from 1 to 6 to get a word from secret list 2: "))]
word3 = list_3[int(input("Type from 1 to 6 to get a word from secret list 3: "))]
word4 = list_4[int(input("Type from 1 to 6 to get a word from secret list 4: "))]
word5 = list_5[int(input("Type from 1 to 6 to get a word from secret list 5: "))]

print ("")

print (f"Twas {word1.upper()}, and the {word2.upper()} toves Did gyre and {word3.upper()} in the wabe:\nAll {word4.upper()} were the borogoves,\nAnd the {word5.upper()} raths outgrabe.\n")

print_the_list = input("Would you like to check the lists? Please type Y or N: ")

if print_the_list.upper() == "Y":
    print(f"\nsecret List 1 = {list_1}\nsecret List 2 = {list_2}\nsecret List 3 = {list_3}\nsecret List 4 = {list_4}\nsecret List 5 = {list_5}\n".upper())
else: 
    print("\nHave a nice day\n")

"""I really appreciate how clear you make your code for a user - 
you've written really good, very specific instructions to them. 
They won't necessarily follow them - but you've given them a lot of guidance!

By asking them to choose a number from 0-5, you've shown how the index position is the key to this activity, 
and you've saved that value to a variable for future use. 
I like the addional if statement at the end - 
we specified that the user shouldn't see the lists before they pick their words, 
but being able to see it after and see what they could have chosen is a nice touch, well done!"""