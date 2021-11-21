#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    r = len(matrix)
    c = len(matrix[0])
    for x in range(r):
        for y in range(c):
            if(y == 0):
                print("{:d}".format(matrix[x][0]), end="")
            else:
                print(" {:d}".format(matrix[x][y]), end="")
        print("\n", end="")
