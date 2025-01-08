lista = [1,2,3,4,5]

slice1 = lista[0:2] #includes de first(index 0), excludes the last

print(slice1) #output: [1,2]

slice2 = lista[:4] #from the first (index 0) item to the list to the last before the parameter after :

print(slice2) #output: [1,2,3,4]

slice3 = lista[2:] #from the 3rd (inclusive) item till the end

print(slice3) #output: [3,4,5]

slice4 = lista[2:4] #from the 2nd (inclusive) to one before the parameter

print(slice4) #output: [3,4]

slice5 = lista[-2:] #from the the second last to the last

print(slice5) #output: [4,5]

slice6 = lista[:-2] #from the first one (index 0) till the third last (it will exclude the second last)

print(slice6) #output: [1,2,3]

slice7 = lista[-4:-1] #from the 4th last to the second last (it will include the first parameter and exclude the last parameter)

print(slice7) #output: [2,3,4]