#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    t = n - 1
    for i in range(n):
        print("{:d}".format(my_list[t]))
        t = t - 1
