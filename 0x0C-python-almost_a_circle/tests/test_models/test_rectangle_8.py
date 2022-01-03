#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.rectangle import Rectangle
"""
test for update 0
"""


class testup(unittest.TestCase):
    def test_update1(self):
        r1 = Rectangle(10, 10, 10, 10)
        a1 = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(r1.__str__(), a1)
        r1.update(89)
        a1 = '[Rectangle] (89) 10/10 - 10/10'
        self.assertEqual(r1.__str__(), a1)
        r1.update(89, 2)
        a1 = '[Rectangle] (89) 10/10 - 2/10'
        self.assertEqual(r1.__str__(), a1)
        r1.update(89, 2, 3)
        a1 = '[Rectangle] (89) 10/10 - 2/3'
        self.assertEqual(r1.__str__(), a1)
        r1.update(89, 2, 3, 4)
        a1 = '[Rectangle] (89) 4/10 - 2/3'
        self.assertEqual(r1.__str__(), a1)


if __name__ == '__main__':
    unittest.main()