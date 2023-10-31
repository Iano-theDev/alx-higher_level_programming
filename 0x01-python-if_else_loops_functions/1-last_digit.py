#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
size = ""
if last_digit > 5:
    size = "and is greater than 5"
elif last_digit == 0:
    size = "and is 0"
else:
    size = "and is less than 6 and not 0"
print(f'Last digit of {number:d} is {last_digit:d} {size}')
