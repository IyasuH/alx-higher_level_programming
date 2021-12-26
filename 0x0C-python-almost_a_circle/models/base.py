#!/usr/bin/python3
"""1 Base class"""


class Base:
    """to manage id attribute in the entrie project and to avoid duplicating the same code"""
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
