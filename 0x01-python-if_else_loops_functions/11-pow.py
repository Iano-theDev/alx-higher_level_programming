#!/usr/bin/python3
def pow(a, b):
    power = 1
    if b < 0:
        for i in range(-b):
            power /= a
        return power
    else:
        for i in range(b):
            power *= a
        return power
