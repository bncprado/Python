import random, colorama

bad_fortunes = [
    "You will experience a minor setback today.",
    "Be cautious, as a challenge is on its way.",
    "Expect some financial difficulties in the near future.",
    "A plan you had will not work out as expected.",
    "You might face unexpected obstacles today.",
]

good_fortunes = [
    "A pleasant surprise awaits you in the coming days.",
    "Your hard work will pay off soon.",
    "Today is a lucky day for you!",
    "An exciting opportunity will come your way.",
    "You will receive good news that brings joy.",
]

user_question = input("Ask me anything and I'll answer you: ")

random_num = random.randint(1,10)

if random_num % 2 == 0:
    print(colorama.Fore.GREEN + good_fortunes[random.randint(0,4)])
else:
    print(colorama.Fore.RED + bad_fortunes[random.randint(0,4)])

