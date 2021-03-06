#!/usr/bin/python3
"""
import modules
"""
import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle
"""
test display 0
"""


class TestRec5(unittest.TestCase):
    """Test for rectangle"""

    def test_display(self):
        """Test for display"""
        r = Rectangle(4, 6)
        new = io.StringIO()
        rec = ('#' * 4 + '\n') * 6
        with redirect_stdout(new):
            r.display()
        self.assertEqual(new.getvalue(), rec)


if __name__ == "__main__":
    unittest.main()
