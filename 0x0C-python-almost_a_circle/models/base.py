#!/usr/bin/python3
"""import modules"""
import json
import os
"""1 Base class"""


class Base:
    """to manage id attribute in the entrie project and
    to avoid duplicating the same code"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of
        list_dictionaries or [] if it is None
        Args:
            list_dictionary - is a list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_obs to a file
        Args:
            list_objs - is a list of instances who inherits of Base
        """
        if list_objs is None:
            with open(cls.__name__ + ".json", mode='w') as file1:
                file1.write("[]")
        else:
            last_list = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__ + ".json", mode='w') as file1:
                file1.write(cls.to_json_string(last_list))

    @staticmethod
    def from_json_string(json_string):
        """This Return the list of the JSON string representation json_string
        or empty list if json_string is None or empty
        Args:
            json_string - is astring representating a list of dictionaries
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attribute already set
        Args:
            **dictionary - used as **kwargs
        """
        if cls.__name__ == "Rectangle":
            rec = cls(12, 4)
            rec.update(**dictionary)
            return rec
        if cls.__name__ == "Square":
            sqr = cls(32)
            sqr.update(**dictionary)
            return sqr

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        Or empty list if file doesn't exit"""
        list_re = []
        name = cls.__name__ + ".json"
        try:
            with open(name, mode='r') as file1:
                list_re = cls.from_json_string(file1.read())
            for i, e in enumerate(list_re):
                list_re[i] = cls.create(**list_re[i])
        except:
            pass
        return list_re
