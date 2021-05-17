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





if __name__ == '__main__':
    unittest.main()
