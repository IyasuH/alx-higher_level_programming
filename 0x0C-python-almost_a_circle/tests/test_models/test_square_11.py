#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.square import Square
from models.base import Base
"""
test for Square size
"""


class testSquSize(unittest.TestCase):
    """test for Square size"""

    def test_setter(self):
        """Test for the setter"""
        s1 = Square(5)
        self.assertEqual(s1._Rectangle__height, 5)

    def test_getter(self):
        """Test for the getter"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)


if __name__ == "__main__":
    unittest.main()
