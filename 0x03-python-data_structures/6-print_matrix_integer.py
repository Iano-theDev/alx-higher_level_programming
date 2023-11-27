#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for line in matrix:
            if not line:
                print()
            for num in line:
                if num is line[-1]:
                    print(num)
                else:
                    print("{:d}, ".format(num), end='')
