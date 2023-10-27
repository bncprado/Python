from colorama import Fore

num = int(input("\nType here your num: "))

if num % 3==0 or num %5 == 0:
    print (f"{Fore.LIGHTGREEN_EX}\nThis number is divisible by 3 or 5\n")
else:
    print (f"{Fore.LIGHTRED_EX}\nThis number is not divisible by 3 or 5\n")