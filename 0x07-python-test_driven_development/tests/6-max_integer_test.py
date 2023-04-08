#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer([..])"""

    def test_max_integer(self):
        """Test method for max_integer"""

        self.assertEqual(max_integer([1,2,3,4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2,-3,4,2,9]), 9)
