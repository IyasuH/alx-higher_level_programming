#!/usr/bin/python3
"""
import modules
"""
import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle
"""
test for display #1
"""


class testDisplay1(unittest.TestCase):
    """Test for Display"""
    def test_display1(self):
        """Test on Display"""
        r = Rectangle(2, 3, 2, 2)
        new = io.StringIO()
        res = ('\n' * 2) + (' ' * 2 + '#' * 2 + '\n') * 3
        with redirect_stdout(new):
            r.display()
        self.assertEqual(new.getvalue(), res)


if __name__ == '__main__':
    unittest.main()
