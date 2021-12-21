#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read a text file and print to stdout
    Args:
        filename - file name"""
    with open(filename, encoding='utf-8', mode='r') as file1:
        print(file1.read(), end="")
