#!/usr/bin/python3
"""import modules"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(list_objs):
        cls = type(list_objs[0]).__name__
        name = "{}.json".format(cls)
        thing = json.loads(list_objs)
        with open(name, mode='w', encoding='utf-8') as file1:
            file1.write(thing)
