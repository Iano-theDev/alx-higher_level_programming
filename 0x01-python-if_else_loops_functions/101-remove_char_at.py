#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for c in range(len(str)):
        if c == n:
            continue
        new_str += str[c]
    return new_str
