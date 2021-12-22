#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """class that defines student"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retives a dictionary repersentation of student"""
        if bool(attrs) and not isinstance(attrs, str)
        and all(isinstance(elem, str) for elem in attrs):
            for i in attrs:
                if hasattr(self, i):
                    return {i: getattr(self, i)}
        else:
            return self.__dict__
