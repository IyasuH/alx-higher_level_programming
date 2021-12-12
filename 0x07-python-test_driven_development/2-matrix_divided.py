#!/usr/bin/python3
"""
Divide a matrx
"""


def matrix_divided(matrix, div):
    """Divides every elemnt of a matrix
    Args:
        matrix: is a list of int or float numbers
        div: is an int or float number that used to
             divide the each elements of the matrix
    """
    new = [x[:] for x in matrix]
    row = len(matrix)
    column = len(matrix[0])
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    for x in range(row):
        if (column != len(matrix[x])):
            raise TypeError("Each row of the matrix must have the same size")
        for y in range(column):
            if (type(matrix[x][y]) != int and type(matrix[x][y]) != float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new[x][y] = round(new[x][y]/div, 2)
    return(new)
