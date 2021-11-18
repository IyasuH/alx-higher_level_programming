#!/usr/bin/python3
import hidden_4


def main():
    start_letter = '__'
    with_s = [x for x in dir(hidden_4) if x.startswith(start_letter)]
    list_s = [x for x in dir(hidden_4) if x not in with_s]
    n = len(list_s)
    for i in range(0, n):
        print(list_s[i])


if __name__ == "__main__":
    main()
