#!/usr/bin/python3
"""A square is a rectsngle"""


class Rectangle:
    """Defines a class based on task number 0
    with private instance attribute width and height
    and this arttribute must be integer and must greater than 0"""

    number_of_instances = 0
    print_symbol = "#"

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
        re = []
        if (self._Rectangle__height is 0):
            return ""
        elif (self._Rectangle__width is 0):
            return ""
        else:
            for y in range(self._Rectangle__height):
                for x in range(self._Rectangle__width):
                    re.append(str(self.print_symbol))
                if y != self._Rectangle__height - 1:
                    re.append("\n")
            return("".join(re))

    def __repr__(self):
        rectangle = "Rectangle(" + str(self._Rectangle__width)
        rectangle += ", " + str(self._Rectangle__height) + ")"
        return(rectangle)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (isinstance(rect_1, Rectangle) is False):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (isinstance(rect_2, Rectangle) is False):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2
            elif rect_2.area() == rect_1.area():
                return rect_1

    @classmethod
    def square(cls, size=0):
        if (type(size) != int):
            raise TypeError("width must be an integer")
        elif (size < 0):
            raise ValueError("width must be >= 0")
        else:
            return cls(size, size)

