#!/usr/bin/python3
"""test the almost a circle project"""


import unittest
from models.base import Base


class TestClassMerthods(unittest.TestCase):
    """test the almost a circle project"""

    def test_Base_id(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(89).id, 89)


    def test_A_nb_objects_private(self):
        '''Tests if nb_objects is private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)


if __name__ == '__main__':
    unittest.main()
