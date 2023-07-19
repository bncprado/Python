"""Figuring out how to append lists inside lists"""

list = [["item"], [0]]
print(list)
list[0].append("item2")
list[1].append(25)
print(list)
