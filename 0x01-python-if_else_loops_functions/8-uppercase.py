#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        char = ord(str[i])
        if ord('a') <= char <= ord('z'):
            char -= 32
        print("{:c}".format(char), end='')
        i += 1
    print()
