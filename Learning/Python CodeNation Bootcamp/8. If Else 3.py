from colorama import Fore

num = int(input(f"{Fore.YELLOW}\nPlease, type a number divisible by 3 or 7 > " ))

if num %7==0 and num %3==0:
    print (f"{Fore.GREEN}\nfizzbuzz\n")

elif num %3==0 :
    print (f"{Fore.CYAN}\nfizz\n") 

elif num %7==0:
    print (f"{Fore.WHITE}\nbuzz\n")

else:
    print  (f"{Fore.RED}\nThe number {num} is not divisible by 3 or 7\n")
