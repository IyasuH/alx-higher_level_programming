#!/usr/bin/python3
"""import module"""
import json
"""From JSON string to object"""


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
