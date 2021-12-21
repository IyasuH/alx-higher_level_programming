#!/usr/bin/python3
"""module import"""
import json
"""create object from a JSON file"""


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename) as file6:
        return json.loads(file6.read())
