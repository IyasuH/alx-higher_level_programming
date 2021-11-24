#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    r = len(matrix)
    c = len(matrix[0])
    sqr = [x[:] for x in matrix]
    for x in range(r):
        for y in range(c):
            sqr[x][y] = sqr[x][y] ** 2
    return(sqr)
