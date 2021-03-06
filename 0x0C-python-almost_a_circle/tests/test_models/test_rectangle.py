#!/usr/bin/pytjon3
"""
importing modules
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
"""
test case for rectangle
"""


class TestRectangle(unittest.TestCase):
    """tests for the rectangle model"""

    def tearDown(self):
        """deleting created instances"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test for First Rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)


if __name__ == '__main__':
    unittest.main()
