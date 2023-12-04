#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for n in my_list:
        x = True if n % 2 == 0 else False
        new_list.append(x)
    return new_list
