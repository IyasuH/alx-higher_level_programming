#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.square import Square
"""
test square update
"""


class testSquareUpdate(unittest.TestCase):
    def test_update(self):
        s1 = Square(5)
        a1 = '[Square] (1) 0/0 - 5'
        self.assertEqual(s1.__str__(), a1)
        s1.update(10)
        a1 = '[Square] (1) 0/0 - 5'
        self.assertEqual(s1.__str__(), a1)
        s1.update(1, 2)
        a1 = '[Square] (1) 0/0 - 2'
        self.assertEqual(s1.__str__(), a1)
        s1.update(1, 2, 3)
        a1 = '[Square] (1) 3/0 - 2'
        self.assertEqual(s1.__str__(), a1)
        s1.update(1, 2, 3, 4)
        a1 = '[Square] (1) 3/4 - 2'
        self.assertEqual(s1.__str__(), a1)
        s1.update(x=12)
        a1 = '[Square] (1) 12/4 - 2'
        self.assertEqual(s1.__str__(), a1)
        s1.update(size=7, y=1)
        a1 = '[Square] (1) 12/1 - 7'
        self.assertEqual(s1.__str__(), a1)
        s1.update(size=7, id=89, y=1)
        a1 = '[Square] (89) 12/1 - 7'
        self.assertEqual(s1.__str__(), a1)


if __name__ == "__main__":
    unittest.main()
