#!/usr/bin/python3
""" Matrix division Module"""


def matrix_divided(matrix, div):
    """
    Divides each element of the matrix with div

    Parameters:
    matrix (list): a list of lists of integers
    div (int): the element to divide by

    Return:
    a list of lists of integers divided with div
    """
    size = None
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if size is None:
            size = len(row)
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for item in row:
                if type(item) is not int and type(item) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise TypeError("division by zero")
    else:
        return [[round(x / div, 2) for x in line] for line in matrix]
