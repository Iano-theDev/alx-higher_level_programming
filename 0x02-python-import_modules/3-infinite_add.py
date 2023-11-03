#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    for num in argv[1:]:
        add += int(num)
    print("{:d}".format(add))
