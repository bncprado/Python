print("""

Create a variable called num.

If num is divisible by 3 print “fizz”, if it's divisible by 7 print “buzz”, if it's divisible by both 3 and 7 print “fizzbuzz”.

Otherwise print num.

""")
      
num = int(input("Please, type a number to check if it's divisible by 3, 7 or 3 and 7: "))

if num%3 == 0 and num%7== 0:
    print("FizzBuzz")
elif num%3 == 0:
    print("Fizz")
elif num%7 == 0:
    print("Buzz")
else:
    print(f"The number {num} is not divisible by 3 or 7")

    