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

    @property
    def size(self):
        """getter to get the value of size"""
        return self._Square__size

    @size.setter
    def size(self, value):
        """setter to change the value os size into value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """function to calculate the area of the square"""
        return (self._Square__size * self._Square__size)
