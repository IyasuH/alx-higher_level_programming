#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """writes to a text file (UTF-8) encoding and returns number of chars
    Args:
        filname - file name
        text - text line"""
    with open(filename, mode='w', encoding='utf-8') as file2:
        return(file2.write(text))
