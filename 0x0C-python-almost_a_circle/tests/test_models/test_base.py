#!/usr/bin/python3
"""test the almost a circle project"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestClassMerthods(unittest.TestCase):
    """test the almost a circle project"""

    def test_Base_id(self):
        self.assertEqual(Base().id, 1)

    def test_Base_id_not_empty(self):
        self.assertEqual(Base(89).id, 89)

    def test_Base_to_json_string(self):
        dictionary = {'id': 12}
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)
        j = '[{"id": 12}]'
        self.assertEqual(json_dictionary, j)

    def test_Base_from_json_string(self):
        json_string = '[{"id": 89}]'
        dictionary = Base.from_json_string(json_string)
        d = [{"id": 89}]
        self.assertEqual(dictionary, d)

    def test_Rectangle(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(type(r), Rectangle)
        self.assertIsInstance(r, Rectangle)

        r1 = Rectangle(1, 2, 3)
        self.assertEqual(type(r1), Rectangle)
        self.assertIsInstance(r1, Rectangle)





if __name__ == '__main__':
    unittest.main()
