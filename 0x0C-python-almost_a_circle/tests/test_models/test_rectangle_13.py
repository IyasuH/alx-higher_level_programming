#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.rectangle import Rectangle
"""
test for Rectangle instance to dictionary representation
"""


class TestRecInstDict(unittest.TestCase):
    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        d1 = r1.to_dictionary()
        self.assertIn('x', d1)
        self.assertIn('y', d1)
        self.assertIn('id', d1)
        self.assertIn('height', d1)
        self.assertIn('width', d1)
        t1 = type(d1)
        self.assertEqual(str(t1), '<class \'dict\'>')
        
if __name__ == "__main__":
    unittest.main()
