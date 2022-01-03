#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.base import Base
"""
Test case for base class
"""


class TestBase(unittest.TestCase):
    """Test for Base model"""
    def test_id(self):
        """Test base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(10)
        self.assertEqual(b3.id, 10)

        b4 = Base()
        self.assertEqual(b4.id, 3)


if __name__ == '__main__':
    unittest.main()
