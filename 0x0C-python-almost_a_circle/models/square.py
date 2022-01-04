#!/usr/bin/python3
"""import module"""
from models.rectangle import Rectangle
"""Square is class that inherit from Rectangle"""


class Square(Rectangle):
    """Args:
           Rectangle - inherited class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Args:
               size - int : the size of square
               x - int
               y - int
        """
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """overloading __str__ method to return
        [Square] (<id>) <x>/<y> - <size>"""
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y, self.height)

    @property
    def size(self):
        """To get the size of square"""
        return self.height

    @size.setter
    def size(self, size):
        """To set the get the value of size
        Args:
            size - size of square"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the attributes from given arguments
        Args:
            *args - none key word arguments
            **kwargs - key word arguments"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.size = args[1]
            if i == 2:
                self.x = args[2]
            if i == 3:
                self.y = args[3]
        if kwargs is not None:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = kwargs.get(k)
                if k == "size":
                    self.size = kwargs.get(k)
                if k == "x":
                    self.x = kwargs.get(k)
                if k == "y":
                    self.y = kwargs.get(k)

    def to_dictionary(self):
        """Returns the dictionary representation of square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
