#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortednames = dict(sorted(a_dictionary.items(), key=lambda x:x[0]))
    for k, v in sortednames.items():
        print('{}:{}'.format(k, v))
