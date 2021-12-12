#!/usr/bin/python3
"""
0-add_integer
Adds two numbers
"""


def add_integer(a, b=98):
    """ Adds two integer or float numbers(a, b) and return their result.
    Args:
        a: must be integer or float type
        b: must be integer or float type and if not given it is 98
    """
    if(type(a) == int):
        a = a
    elif(type(a) == float):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if (a is None and b == 98):
        raise TypeError("a must be an integer")
    if(type(b) == int):
        b = b
    elif(type(b) == float):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return (a + b)
