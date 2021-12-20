#!/usr/bin/python3
"""only sub class of"""


def inherits_from(obj, a_class):
    """ True if the object is an instance of class
    that inherited from the specified class
    Args:
        obj - object
        a_class - class"""
    if issubclass(a_class, (a_class, obj)) and type(obj) is not a_class:
        return True
    return False
