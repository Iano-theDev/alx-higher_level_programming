#!/usr/bin/python3
import random
number = random.randint(-10, 10)
sign = ""
if number > 0:
    sign = "is positive"
elif number == 0:
    sign = "is zero"
else:
    sign = "is negative"
print(f'{number:d} {sign}')
