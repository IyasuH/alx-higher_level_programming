#!/usr/bin/python3
"""String representation"""


class Rectangle:
    """Defines a class based on task number 0
    with private instance attribute width and height
    and this arttribute must be integer and must greater than 0"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self._Rectangle__width = width
        self._Rectangle__height = height
        type(self).number_of_instances += 1

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
        if (self._Rectangle__height is 0):
            return 0
        elif (self._Rectangle__width is 0):
            return 0
        else:
            return (self._Rectangle__height * 2 + self._Rectangle__width * 2)

    def __str__(self):
        re = ""
        if (self._Rectangle__height is 0):
            return ""
        elif (self._Rectangle__width is 0):
            return ""
        else:
            for y in range(self._Rectangle__height):
                for x in range(self._Rectangle__width):
                    re = re + "#"
                re += '\n'
            re = re[:-1]
            return(re)

    def __repr__(self):
        rectangle = "Rectangle(" + str(self._Rectangle__width)
        rectangle += ", " + str(self._Rectangle__height) + ")"
        return(rectangle)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
