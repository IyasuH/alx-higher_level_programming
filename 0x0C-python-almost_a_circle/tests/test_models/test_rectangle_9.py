#!/usr/bin/puthon3
"""
import modules
"""
import unittest
from models.rectangle import Rectangle
"""
test for update#1
"""


class TestUp(unittest.TestCase):
    def test_update1(self):
        r = Rectangle(10, 10, 10, 10)
        a = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(r.__str__(), a)
        r.update(height=1)
        a = '[Rectangle] (1) 10/10 - 10/1'
        self.assertEqual(r.__str__(), a)
        r.update(width=1, x=2)
        a = '[Rectangle] (1) 2/10 - 1/1'
        self.assertEqual(r.__str__(), a)
        r.update(y=1, width=2, x=3, id=89)
        a = '[Rectangle] (89) 3/1 - 2/1'
        self.assertEqual(r.__str__(), a)
        r.update(x=1, height=2, y=3, width=4)
        a = '[Rectangle] (89) 1/3 - 4/2'
        self.assertEqual(r.__str__(), a)


if __name__ == '__main__':
    unittest.main()
