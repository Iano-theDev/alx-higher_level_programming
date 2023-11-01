#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j and i < 8:
            print("{:d}{:d}, ".format(i, j), end='')
        elif i < j:
            print("{:d}{:d}".format(i, j))
