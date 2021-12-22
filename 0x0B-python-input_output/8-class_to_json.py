#!/usr/bin/python3
"""Class to json"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object
    Args:
        obj - is aninstance of a class"""
    return obj.__dict__
