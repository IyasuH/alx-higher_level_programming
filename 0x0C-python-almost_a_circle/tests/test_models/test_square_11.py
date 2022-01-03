#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.square import Square
"""
test for Square size
"""


class testSquSize(unittest.TestCase):
    def test_setter(self):
        s1 = Square(5)
        self.assertEqual(s1._Rectangle__height, 5)

    def test_getter(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)


if __name__ == "__main__":
    unittest.main()
