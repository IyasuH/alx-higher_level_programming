#!/usr/bin/python3
"""
Max integer
"""


def max_integer(list=[]):
    """To find maximum elment from the given list
    Args:
        list = []
    """
    if (len(list) == 0):
        return None
    else:
        high = list[0]
        for i in list:
            if (i > high):
                high = i
        return(high)
