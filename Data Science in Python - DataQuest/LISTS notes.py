list_a = [5,6,7,8,9]
list_b = ["1", "2", "3", "4", "5"]
list_cd = [[1,2,3,4,5],["a", "b", "c", "d", "e"]]

# print(list_a[0])#prints first item of the list
# print(list_b[0])#prints first item of the list
# print(list_cd[1])#prints the second item (that is a list) of the list
# print(list_cd[1][0])#prints first item of the second list
# print(sum(list_a)) #prints the sum of all items (if numbers or float) inside the list


# CONVERTING STRINGS INSIDE OF LISTS TO NUMBERS. 
emptylist = []
for strings in list_b:
  emptylist.append(int(strings))


print(sum(emptylist))




