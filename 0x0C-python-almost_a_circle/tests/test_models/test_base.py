#!/usr/bin/python3
"""test the almost a circle project"""


import unittest
from models.base import Base


class TestClassMerthods(unittest.TestCase):
    """test the almost a circle project"""

    def test_Base_id(self):
        self.assertEqual(Base().id, 1)

    def test_Base_id_not_empty(self):
        self.assertEqual(Base(89).id, 89)





if __name__ == '__main__':
    unittest.main()
