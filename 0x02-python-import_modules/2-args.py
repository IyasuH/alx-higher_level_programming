#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    args = argv
    n = len(args)
    if (n == 1):
        print("0 arguments.")
    elif (n == 2):
        print("1 argument:")
        print("{}: {}".format(1, argv[1]))
    else:
        print("{} arguments:".format(n - 1))
        for i in range(1, n):
            print("{}: {}".format(i, argv[i]))
