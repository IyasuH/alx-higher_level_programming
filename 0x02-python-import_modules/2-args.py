#!/usr/bin/python3
import sys


def main():
    args = sys.argv
    n = len(args)
    if (n == 1):
        print("0 arguments.")
    else:
        print("{} arguments:".format(n - 1))
        for i in range(1, n):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
