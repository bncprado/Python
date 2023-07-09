import datetime

shop = {
    'apple': 0.99,
    'banana': 0.5,
    'orange': 0.75,
    'milk': 2.49,
    'bread': 1.99,
    'eggs': 2.99,
    'chicken': 5.99,
    'beef': 7.99,
    'pork': 6.99,
    'potato': 0.79,
    'tomato': 1.29,
    'onion': 0.89,
    'carrot': 0.99,
    'lettuce': 1.49,
    'cheese': 3.99,
    'yogurt': 2.79,
    'chocolate': 3.49,
    'ice cream': 4.99,
    'coffee': 4.49,
    'tea': 3.29
}

current_time = datetime.datetime.now().time().hour

def greetings():
    if current_time >= 0 and current_time < 12:
        print ("Good morning. Welcome to Bruno Groceries.")
    elif current_time >= 12 and current_time < 18:
        print ("Good afternoon. Welcome to Bruno Groceries.")
    else:
        print ("Good evening. Welcome to Bruno Groceries.")

greetings()
