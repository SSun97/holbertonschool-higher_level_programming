#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer.py"""

    def test_max_integer(self):
        """Test method max_integer(list=[])"""

        self.assertEqual(4, max_integer([1, 2, 3, 4]))
        self.assertEqual(4, max_integer([1, 2, 4, 3]))

if __name__ == '__main__':
    unittest.main()
