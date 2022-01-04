#!/usr/bin/python3
"""import module"""
from models.base import Base
"""Rectangle class that inherits from Base"""


class Rectangle(Base):
    """Args:
           base - class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Args:
               width - int : width of rectangle
               height - int : height of rectangle
               x - int
               y - int
               id - int
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """To get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """To set the width of the rectangle
        Args:
            width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """To get the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """To set the height of rectangle
        Args:
           height"""
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """To get the x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """To set the value of x
        Args:
            x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """To get the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """To set the value of y
        Args:
            y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """To get the area of rectangle"""
        area = self.__width * self.__height
        return area

    def display(self):
        """To display the rectangle using #"""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for n in range(self.__width):
                print("#", end="")
            print("\n", end="")

    def __str__(self):
        """overriding the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute or assign a
        a key/value argument to the attribute
        Args:
            *args - non key word argument
            **kwargs - keyword argument"""
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
        """Returns the dictionary representation of
        a rectangle"""
        return {'id': self.id, 'width': self.__width, 'height':
                self.__height, 'x': self.__x, 'y': self.__y}
