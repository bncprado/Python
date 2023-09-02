## 1. Storing Data ##

content_ratings = ['4+', '9+', '12+', '17+']
numbers = [4433, 987, 1155, 622]
content_rating_numbers = [['4+', '9+', '12+', '17+'], [4433, 987, 1155, 622]]

## 2. Dictionaries ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
print(content_ratings)

## 3. Indexing ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
over_9=content_ratings['9+']
over_17=content_ratings['17+']
                        
print(over_9, over_17)                 

## 4. Alternative Method of Creating a Dictionary ##

content_ratings={}
content_ratings['12+'] = 1155
content_ratings['17+'] = 622
content_ratings['4+'] = 4433
content_ratings['9+'] = 987
over_12_n_apps = content_ratings['12+']

## 5. Key-Value Pairs ##

error = True

## 6. Key-Value Pairs Continued ##

d_1={'key_1':'first_value',
     'key_2': 2,
     'key_3': 3.14,
     'key_4': True, 
     'key_5': [4,2,1],
     'key_6': {'inner_key':6}
    }