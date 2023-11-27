#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        if line:
            print(", ".join("{:d}".format(num) for num in line), end='')
        print()
