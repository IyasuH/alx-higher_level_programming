#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle:
    """Defines a class based on task number 0
    with private instance attribute width and height
    and this arttribute must be integer and must greater than 0"""
    def __init__(self, width=0, height=0):
        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
    def area(self):
        """To calculate the area of the rectangle"""
        return (self._Rectangle__height * self._Rectangle__width)
    def perimeter(self):
        """To calculate the perimeter of the rectangle"""
        return (self._Rectangle__height*2 + self._Rectangle__width *2)
