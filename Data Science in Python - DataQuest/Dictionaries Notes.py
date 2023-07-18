# # We use the in operator to check if something is inside the dictionary, if the dictionary has what we want, it will return "True. Otherwise, false e.g."
# content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

# print('10+' in content_ratings)
# print('12+' in content_ratings)

# #--------------------------------------------------------------------------------

# Checking if 4433 or 987 exists in content_ratings also returns False because the search is only for the dictionary's keys (4433 and 987 exist as dictionary values in content_ratings).

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

print(4433 in content_ratings)
print(987 in content_ratings)

#--------------------------------------------------------------------------------
