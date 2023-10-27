from colorama import Fore, init
init(autoreset=True)

while True:
    answer = input(f"{Fore.YELLOW}\nWhat's the capital of England?\n\nType your answer here: ").lower()
    if answer == "london":
        print (f"{Fore.GREEN}\nCorrect! The answer is {answer.title()}\n")
        quit()
    else:
        print (f"{Fore.RED}\nIncorrect! The capital of England is not {answer.title()}. Try again.")
