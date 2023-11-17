#!/usr/bin/env python
# coding: utf-8

# ## Analyzing apps (1 of 14)

# We only build apps that are free to download and install, and our main source of revenue consists of in-app ads. This means that the number of users of our apps determines our revenue for any given app — the more users who see and engage with the ads, the better. Our goal for this project is to analyze data to help our developers understand what type of apps are likely to attract more users

# ### Block of code to open CSV file(s) (2 of 14)

# In[1]:


from csv import reader
opened_file_ios = open("AppleStore.csv", encoding='utf8')
opened_file_android = open("googleplaystore.csv", encoding='utf8')
read_file_ios = reader(opened_file_ios)
read_file_android = reader(opened_file_android)
ios = list(read_file_ios)
android = list(read_file_android)
ios_data = ios[1:]
android_data = android[1:]


# ### Useful functions to check the index number for each dataset (2 of 14)

# In[2]:


def ios_index_identifier():
    z=0
    if z == 0:
        print('IOS INDEX NUMBER IDENTIFIER\n')
    for x in ios[:1][0]:
        print(f"{z} = {x}")
        z+=1
        
def android_index_identifier():
    z=0
    if z == 0:
        print('ANDROID INDEX NUMBER IDENTIFIER\n')
    for x in android[:1][0]:
        print(f"{z} = {x}")
        z+=1


# ### The following function opens a dataset, based on start and end index parameters, and print the rows and collumns of the dataset if the argument 'True' is also passed: (2 of 14)

# In[3]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))


# ### Testing the function 'explore_data', IOS and Android index identifiers (2 of 14)
# #### Note the number of rows:

# In[4]:


ios_index_identifier()
print('')
explore_data(ios_data, 0,2, True)
print('')
android_index_identifier()
print('')
explore_data(android_data, 0,2, True)


# ### Deleting the row that has wrong data (3 of 14)

# In[5]:


del android_data[10472]


# ### The dataset now has one row less. (3 of 14)

# In[6]:


explore_data(android_data, 10472,10473, True)


# ### Finding duplicate entries on "android_apps" (4 of 14)
# #### The code below is indexing the duplicated apps in a separated list named 'duplicated_apps'. 
# The Android dataset has some duplicated apps. So we're removing them. You can get more info in the next blocks of codes

# In[7]:


unique_apps=[]
duplicated_apps=[]

for row in android_data:
    name = row[0]
    if name not in unique_apps:
        unique_apps.append(name)
    elif name in unique_apps:
        duplicated_apps.append(name)


# ### Now, let's print the number of  duplicated and unique apps and some examples:

# In[8]:


print(f'Number of duplicated apps: {len(duplicated_apps)}')


# #### Some examples of duplicated apps:

# In[9]:


for row in duplicated_apps[:15]:
    print(row)


# ### To select and delete the 'right' duplicated app, we determined the ones with the highest number of reviews as the most recent ones. After isolating them, we added each particular one to a dictionary named "reviews_max" (5 of 14)

# In[10]:


reviews_max={}

for row in android_data:
    name = row[0]
    n_reviews = float(row[3])
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    elif name not in reviews_max:
        reviews_max[name] = n_reviews


# ### Now, we are checking if the Android dataset (without the header) minus the duplicated apps has the same number of entries as the newly created 'reviews_max' dictionary

# In[11]:


print(f"Android dataset(10840) - duplicated apps length(1181) = {len(android_data)-1181}")
print(f"'reviews_max' dictionary length = {len(reviews_max)}")


# ### Separating the unique apps to a new list (5 of 14)

# In[12]:


android_clean=[]

already_added=[]

for row in android_data:
    name = row[0]
    n_reviews = float(row[3])
    
    if reviews_max[name] == n_reviews and name not in already_added:
        android_clean.append(row)
        already_added.append(name)

   


# ### Checking if the new list has the same number of entries as our dictionary 'reviews_max'

# In[13]:


explore_data(android_clean,0,1,True)


# ### Removing non-English apps (6 of 14)
# #### The function underneath takes a string as a parameter and check if the string has non-English characters
# Some apps are named in English, but they have some different characters or emojis that might confuse our function and make it realise that is a non-English app. To solve that problem, we are looking for apps that have more than three non-English characters. This way we might have a better filter to determine if the app is named with non-English characters. 
# 
# 
# Note that the function has a built-in function 'ord()' inside

# In[14]:


def check_char(string):
    count = 0
    for x in string:
        if ord(x) > 127:
            count += 1
            if count > 3:
                return False
    return True


# #### Testing the function 'check_char()'

# In[15]:


check_char('Instagram')


# In[16]:


check_char('爱奇艺PPS -《欢乐颂2》电视剧热播')


# In[17]:


check_char('Docs To Go™ Free Office Suite')


# In[18]:


check_char('Instachat 😜')


# ### Using the function to remove non-English apps from the 'android_clean' and 'ios_data' datasets:

# In[19]:


android_clean_english=[]
ios_clean_english=[]

for row in android_clean:
    name=row[0]
    if check_char(name):
        android_clean_english.append(row)
        
for row in ios_data:
    name=row[1]
    if check_char(name):
        ios_clean_english.append(row)        

    


# ### Checking the new numbers with the non-English apps removed

# In[20]:


explore_data(android_clean_english,0,1,True)
explore_data(ios_clean_english,0,1,True)


# ### Isolating the IOS and Android free apps to new lists
# Also checking how many apps we have left

# In[21]:


ios_free_apps=[]

for row in ios_clean_english:
    price = float(row[4])
    if price == 0.0:
        ios_free_apps.append(row)
        
explore_data(ios_free_apps,0,1,True)


# In[22]:


android_free_apps=[]

for row in android_clean_english:
    price = row[6]
    if price == "Free" or price == 'free':
        android_free_apps.append(row)
        
explore_data(android_free_apps,0,1,True)


# As we mentioned in the introduction our goal is to determine the kinds of apps that are likely to attract more users because the number of people using our apps affect our revenue.
# 
# To minimize risks and overhead, our validation strategy for an app idea has three steps:
# 
# 1- Build a minimal Android version of the app, and add it to Google Play.
# 
# 2- If the app has a good response from users, we develop it further.
# 
# 3- If the app is profitable after six months, we build an iOS version of the app and add it to the App Store.
# 
# Because our end goal is to add the app on both Google Play and the App Store, we need to find app profiles that are successful in both markets. For instance, a profile that works well for both markets might be a productivity app that makes use of gamification.

# #### Creating a frequency dictionary for genre in the IOS dataset:

# In[23]:


ios_genre_list={}

for row in ios_free_apps:
    genre = row[11]
    if genre in ios_genre_list:
        ios_genre_list[genre]+=1
    else:
        ios_genre_list[genre]=1
        
for x in ios_genre_list:
    print(f"{x}: {ios_genre_list[x]}")


# #### Creating a frequency dictionary for genre and another one for category in the Android dataset:

# In[24]:


android_genre_list={}

for row in android_free_apps:
    genre = row[9]
    if genre in android_genre_list:
        android_genre_list[genre]+=1
    else:
        android_genre_list[genre]=1
        
# for x in android_genre_list:
#     print(f"{x}: {android_genre_list[x]}")


# In[25]:


android_category_list={}

for row in android_free_apps:
    category = row[1]
    if category in android_category_list:
        android_category_list[category]+=1
    else:
        android_category_list[category]=1
        
# for x in android_category_list:
#     print(f"{x}: {android_category_list[x]}")  


# In[26]:


def freq_table(dataset, index):
    for row in dataset[index]:
        
        
        
    

