#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """return True if the object is an instance of
    a class that inherited from the specified class
    Args:
        obj - object
        a_class - class"""
    return isinstance(obj, a_class)
