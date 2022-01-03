#!/usr/bin/python3
"""import module"""
from models.base import Base

"""Rectangle class that inherits from Base"""


class Rectangle(Base):
    """Args:
           base - class """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be > 0")
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def area(self):
        area = self.__width * self.__height
        return area

    def display(self):
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for n in range(self.__width):
                print("#", end="")
            print("\n", end="")

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'
        .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.__width = args[1]
            if i == 2:
                self.__height = args[2]
            if i == 3:
                self.__x = args[3]
            if i == 4:
                self.__y = args[4]
        if kwargs is not None:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = kwargs.get(k)
                if k == "width":
                    self.__width = kwargs.get(k)
                if k == "height":
                    self.__height = kwargs.get(k)
                if k == "x":
                    self.__x = kwargs.get(k)
                if k == "y":
                    self.__y = kwargs.get(k)

    def to_dictionary(self):
        return {'id': self.id, 'width': self.__width, 'height':
                self.__height, 'x': self.__x, 'y': self.__y}
