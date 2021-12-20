#!/usr/bin/python3
"""Integer validator"""


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
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
