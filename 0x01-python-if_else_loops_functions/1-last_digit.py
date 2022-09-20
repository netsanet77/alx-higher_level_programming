#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    Ldigit = -(-number % 10)
else:
    Ldigit = (number % 10)
if Ldigit > 5:
    print(f"Last digit of {number} is {Ldigit} and is greater than 5")
elif Ldigit == 0:
    print(f"Last digit of {number} is {Ldigit} and is 0")
else:
    print(f"Last digit of {number} is {Ldigit} and is less than 6 and not 0")
