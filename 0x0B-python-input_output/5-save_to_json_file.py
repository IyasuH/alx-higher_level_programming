#!/usr/bin/python3
"""import Module"""
import json
"""Save Object to a file"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open(filename, mode='w') as file5:
        file5.write(json.dumps(my_obj))
