#!/usr/bin/python3
import sys


def main():
    args = sys.argv
    n = len(args)
    sum = 0
    if (n == 1):
        print("0")
    else:
        for i in range(1, n):
            sum = sum + int(sys.argv[i])
        print(sum)


if __name__ == "__main__":
    main()
