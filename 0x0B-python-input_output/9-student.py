#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """class that defines student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retives a dictionary repersentation of student"""
        return self.__dict__
