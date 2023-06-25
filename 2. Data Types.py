#numeric
integer_type = 5
float_type = 5.5
complex_type = 'I need to study about this one later'

'''
Boolean Type:

bool: Represents boolean values True or False. It is useful for logical operations and conditional statements.
Sequence Types:
'''
boolean_type_true = True
boolean_type_false = False

'''
str: Represents a sequence of characters, such as "Hello, world!" or 'OpenAI'.
'''

string_type = "any text between single or double quotes"

'''
list: Represents an ordered collection of items. It can contain elements of different data types. Lists are mutable, meaning you can modify their contents.
'''
list = [
    24,
    34,
    54,
    'item1',
    'item2',
    True
]

list.insert(1,'inserted') #changing the list 

print(list)

'''
tuple: Similar to lists, tuples are ordered collections of items. However, they are immutable, meaning their contents cannot be changed once defined.
'''
tuple = (
    24,
    34,
    54,
    'item1',
    'item2',
    True
)

print(tuple)

tuple.insert(1, 'inserted')

print (tuple)
'''
Mapping Type:

dict: Represents a collection of key-value pairs. It is an unordered data type, where each key is associated with a value. Dictionaries are mutable.
Set Types:

set: Represents an unordered collection of unique elements. Sets are useful for operations like union, intersection, and difference.
frozenset: Similar to sets, frozensets are immutable.
None Type:

None: Represents the absence of a value. It is often used to indicate the absence of a return value or as a default value.
'''