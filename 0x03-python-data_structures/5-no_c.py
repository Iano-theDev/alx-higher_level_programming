#!/usr/bin/python3
def no_c(my_string):
    new_list = ''
    for c in my_string:
        if c == 'c' or c == 'C':
            continue
        else:
            new_list += c
    return new_list
