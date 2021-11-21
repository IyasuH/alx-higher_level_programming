#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    r = len(matrix)
    c = len(matrix[0])
    n = 0
    for x in range(r):
        n += 1
        for y in range(c):
            print("{:d}".format(matrix[x][y]), end=" ")
        print("\n", end="")
