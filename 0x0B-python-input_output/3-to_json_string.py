#!/usr/bin/python3
"""importing module"""
import json
"""To JSON string"""


def to_json_string(my_obj):
    """return the JSON repersentation of an object"""
    return json.dumps(my_obj)
