#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.base import Base


class TestFileToIn(unittest.TestCase):
    """Test for File to instances"""
    def test_load_from_file(self):
        """Test for load_from_file"""
        r1 = Rectangle(10, 7, 2, 8)

if __name__ == "__main__":
    unittest.main()
