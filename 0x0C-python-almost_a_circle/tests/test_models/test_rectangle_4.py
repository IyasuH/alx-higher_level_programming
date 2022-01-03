#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.rectangle import Rectangle
"""
test for area first
"""


class TestRec4(unittest.TestCase):
    """Test for Rectangle model"""
    def test_Area_first(self):
        """Area first test"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)


if __name__ == "__main__":
    unittest.main()
