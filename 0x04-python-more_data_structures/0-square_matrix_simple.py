#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for n in matrix:
        result.append(list(map(lambda x: x * x, n)))
    return result
