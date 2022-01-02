#!/usr/bin/pytjon3
"""
importing modules
"""
import unittest
from models.rectangle import Rectangle
"""
test case for rectangle
"""


class TestRectangle(unittest.TestCase):

    def test_first(self):
        r1 = Rectangle(10, 2)
        self.assertAlmostEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertAlmostEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertAlmostEqual(r3.id, 12)


if __name__ == '__main__':
    unittest.main()
