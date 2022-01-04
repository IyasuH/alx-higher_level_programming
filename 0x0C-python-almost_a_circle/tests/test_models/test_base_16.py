#!/usr/bin/python3
"""
import models
"""
import unittest
from models.rectangle import Rectangle
"""
Test for JSON string to file
"""


class TestJSONstr(unittest.TestCase):
    """Test for JSON string to file"""
    def test_save_to_file(self):
        """Test for save to file function"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])


if __name__ == '__main__':
    unittest.main()
