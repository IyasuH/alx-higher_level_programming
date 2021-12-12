#!/usr/bin/python3
"""
Unittest for max_integer([.,])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TesetMaxInteger(unittest.TestCase):
    def __init__(self):
        self.assertAlmostEqual(max_integer([1,2,3,4,5]),5)
        self.assertAlmostEqual(max_integer([78,-23,45,89]),89)
