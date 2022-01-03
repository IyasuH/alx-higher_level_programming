#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.rectangle import Rectangle
"""
test for __str__
"""


class test_str(unittest.TestCase):
    """Test on __str___ """
    def test_str(self):
        """test for __str__ method"""
        r = Rectangle(4, 6, 2, 1, 12)
        res = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(r.__str__(), res)


if __name__ == '__main__':
    unittest.main()
