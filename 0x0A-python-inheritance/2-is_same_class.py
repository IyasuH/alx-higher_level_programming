#!/usr/bin/python3
"""My list"""
def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class
    Args:
        obj - object
        a_class - class"""
    result = isinstance(obj, a_class)
    if result and type(obj) is a_class:
        return True
    else:
        return False

