#!/usr/bin/python3
"""import 9-rectangle module"""
Rectangle = __import__('9-rectangle').Rectangle
"""Square"""


class Square(Rectangle):
    def __init__(self, size):
        """inherits from rectangle(9-rectangle.py)
        Args:
            size - must be positve integer"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
