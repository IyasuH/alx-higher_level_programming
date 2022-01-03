#!/usr/bin/python
"""
import modules
"""
import unittest
from models.rectangle import Rectangle
"""
test for validate sttributes task
"""


class TestRec3(unittest.TestCase):
    """Test rectangle"""
    def test_validate(self):
        """test validate attributes"""
        with self.assertRaises(TypeError):
            Rectangle(10, "3")
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)


if __name__ == '__main__':
    unittest.main()
