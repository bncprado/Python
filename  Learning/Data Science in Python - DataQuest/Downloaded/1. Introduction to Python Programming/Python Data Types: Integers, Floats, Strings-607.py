## 1. Integers and Floats ##

personal_apps = 0
personal_apps += 1.99
gift_apps = 6.99
gift_apps *= 3
print(personal_apps)
print(gift_apps)

## 2. Conversion Between Types ##

personal_apps = 0
personal_apps += 1.99

gift_apps = 6.99
gift_apps *= 3 

print(personal_apps)
print(gift_apps)

# Update the values of personal_apps and gift_apps
# Write your code below this line

personal_apps = round(personal_apps)
gift_apps = int(gift_apps)

print(personal_apps)
print(gift_apps)

## 3. Strings ##

app_name = "Minecraft: Pocket Edition"
average_rating = "4.5"
total_ratings = "522012"
print(app_name)

## 4. Escaping Special Characters ##

motto = "Facebook's new motto is \"move fast with stable infra.\"" 
print(motto)

## 5. String Concatenation ##

facebook = "Facebook's rating is"
fb_rating_str = "3.5"
fb = facebook + " " + fb_rating_str
print(fb) 

## 6. String Conversion ##

facebook = "Facebook's rating is"
fb_rating = 3.5
fb_rating_str = str(fb_rating)
fb = facebook + " " + fb_rating_str
print(fb)

## 7. Multi-line Strings ##

motto = '''
Facebook's old motto was 'move fast and break things'.
Facebook's new motto is 'move fast with stable infra'.
'''
print(motto)