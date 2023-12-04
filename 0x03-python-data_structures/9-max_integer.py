#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        a = my_list[0]
        for n in my_list:
            if n > a:
                a = n
        return a
    return None
