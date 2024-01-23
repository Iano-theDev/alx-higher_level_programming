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
    new_matrix = []
    div_list = [div]
    for n in matrix:
        new_matrix.append(list(map(lambda a, b: a / b, n, div_list)))
    return new_matrix
