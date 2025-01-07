owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners,dogs_names) #it combines the two lists into a new list

print(names_and_dogs_names) #it's going to print "<zip object at 0x1008ba9c0>". This zip object contains the location of this variable in our computer’s memory. Don’t worry though, it is fairly simple to convert this object into a useable list by using the built-in function list():

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names) #Notice two things: 1.Our data set has been converted from a zip memory object to an actual list (denoted by [ ]), 2.Our inner lists don’t use square brackets [ ] around the values. This is because they have been converted into tuples (an immutable type of list).