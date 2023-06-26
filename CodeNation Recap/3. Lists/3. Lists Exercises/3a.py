print("""

Create a list of your three favourite websites and then add another two using a method.

Then, remove the last website using a method.

""")
      
favourite_websites = [
    "YouTube",
    "FaceBook",
    "Spotify"
]

print(favourite_websites)

favourite_websites.append("Gmail")
favourite_websites.append("Ebay")

print(favourite_websites)

favourite_websites.pop(-1) #using -1 just for the sake of remembering

print(favourite_websites)