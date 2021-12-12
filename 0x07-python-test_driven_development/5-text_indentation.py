#!/usr/bin/python3
"""
Text indentation
"""


def text_indentation(text):
    """ Prints a text with 2 new lines afte
        each of these charachters '.' '?' and ':'
    Args:
        text: must be string otherwise raise TypeError
    """
    if (type(text) is not str):
        raise TypeError("text must be a string")
    n = len(text)
    new = ""
    for c in range(n):
        if (text[c-1] is '.' or text[c-1] is '?' and text[c] is ' '):
            new += '\n'
            new += '\n'
        elif (text[c-1] is ':' and text[c] is ' '):
            new += '\n'
            new += '\n'
        else:
            new += text[c]
    print(new, end="")
