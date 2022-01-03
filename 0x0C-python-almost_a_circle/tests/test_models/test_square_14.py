#!/usr/bin/python
"""
import modules
"""
import unittest
from models.square import Square
"""
test for models.square import Square
"""


class TestSquareInstDict(unittest.TestCase):
    def t0_dictionary(self):
        s1 = Square(10, 2, 1)
        d1 = s1.to_dictionary()
        self.assertIn('id', d1)
        self.assertIn('size', d1)
        self.assertIn('x', d1)
        self.assertIn('y', d1)
        t1 = type(d1)
        self.assertEqual(str(t1), '<class \'dict\'>')


if __name__ == "__main__":
    unittest.main()
