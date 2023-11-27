#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    text = ""
    for line in matrix:
        if not line:
            text += "\n"
            continue
        text += "{:d}".format(line[0])
        for i in range(1, len(line)):
            text += " {:d}".format(line[i])
        text += "\n"
    print(text, end="")
