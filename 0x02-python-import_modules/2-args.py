#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = 0
    len_args = len(argv) - 1
    if len_args == 0:
        print("0 arguments.")
    elif len_args == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len_args - 1))
    while count < len_args:
        print("{:d}: {}".format(count + 1, len_args + 1))
        count += 1
