#!/usr/bin/python3
"""
import modules
"""
import unittest
import io
from contextlib import redirect_stdout
from models.square import Square
"""
test for task 10 square
"""


class TestSquare(unittest.TestCase):
    def test_square_10(self):
        s1 = Square(5)
        a1 = '[Square] (1) 0/0 - 5'
        self.assertEqual(s1.__str__(), a1)
        self.assertEqual(s1.area(), 25)
        new = io.StringIO()
        dis = ('#' * 5 + '\n') * 5
        with redirect_stdout(new):
            s1.display()
        self.assertEqual(new.getvalue(), dis)


if __name__ == '__main__':
    unittest.main()
