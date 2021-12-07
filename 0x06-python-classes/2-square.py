#!/usr/bin/python3
"""a module that defines a class Square"""


class Square:
    """a class that defines a square by based on 1-square.py
    private instanve attribure size
    with out any module"""
    def __init__(self, size=0):
        """size must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer
        if size is less than 0, raise a ValueError exception
        with the message size must be >= 0
        """
        self._Square__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
