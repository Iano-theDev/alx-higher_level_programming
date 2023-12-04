#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for n in my_list:
        x = n % 2
        new_list.append(x)
    return new_list
