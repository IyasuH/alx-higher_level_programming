#!/usr/bin/python3
"""import module"""
from models.rectangle import Rectangle
"""Square is class that inherit from Rectangle"""


class Square(Rectangle):
    """Args:
           Rectangle - inherited class"""
    def __init__(self, size, x=0, y=0, id=None):
        super(Square, self).__init__(self, size, x, y, id)
        self.height = size
        self.width = size

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'
        .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
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
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
