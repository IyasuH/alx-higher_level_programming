#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file and returns number of char
    Args:
        filename - file name
        text - text"""
    with open(filename, mode="a", encoding="utf-8") as file3:
        return (file3.write(text))
