#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""
test for  Dictionary to JSON string
"""


class TestDicToJson(unittest.TestCase):
    """Test for  Dictionary to JSON string"""
    def t0_json_string(self):
        """Test for to_json_string"""
        r1 = Rectangle(10, 7, 2, 8)
        d1 = r1.to_dictionary()
        t1 = type(d1)
        self.assertEqual(str(t1), '<class \'dict\'>')
        json_dictionary = Base.to_json_string([dictionary])
        t2 = type(json_dictionary)
        self.assertEqual(str(t2), '<class \'str\'>')


if __name__ == '__main__':
    unittest.main()
