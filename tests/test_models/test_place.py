#!/usr/bin/python3

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def setUp(self):
        self.my_place = Place()

    def test_attributes_initialization(self):
        self.assertEqual(self.my_place.name, "")

if __name__ == '__main__':
    unittest.main()