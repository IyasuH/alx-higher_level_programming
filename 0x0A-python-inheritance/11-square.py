#!/usr/bin/python3


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """raise Exception: area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """"public instance method that validates value
        Args:
            name - is always string
            value - greter than 0 int"""
        self.name = name
        self.value = value
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """width ad height must be positive integers
        validate by integer_validator"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return"[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square-11"""
    def __init__(self, size):
        """inherits from rectangle(9-rectangle.py)
        Args:
            size - must be positve integer"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)
        super().area()

    def __str__(self):
        """return string """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
