#!/usr/bin/python3
"""a module that defines a class Square"""


class Square:
    """a class that defines a square by based on 1-square.py
    private instanve attribure size
    with out any module"""
    def __init__(self, size=0, position=(0, 0)):
        """size must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer
        if size is less than 0, raise a ValueError exception
        with the message size must be >= 0
        """
        self._Square__size = size
        self._Square__position = position
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

    @property
    def position(self):
        """getter to get the value of position"""
        return self._Square__position

    @position.setter
    def position(self, value):
        """setter to set the value position"""
        if (value[0] or value[1] is not int or value[0] or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value

    def area(self):
        """function to calculate the area of the square"""
        return (self._Square__size * self._Square__size)

    def my_print(self):
        """function that prints in stdout the square with the character #"""
        if self._Square__size is 0:
            print("")
        else:
            for x in range(self._Square__size):
                for y in range(self._Square__size):
                    for a in range(self._Square__position[0]):
                        if y is not 0:
                            break
                        print("_", end="")
                    print("#", end="")
                print("\n", end="")
