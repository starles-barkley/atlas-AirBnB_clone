#!/usr/bin/python3

import unittest
from models.city import City

class TestState(unittest.TestCase):

    def setUp(self):
        self.my_city = City()

    def test_attributes_initialization(self):
        self.assertEqual(self.my_city.name, "")

if __name__ == '__main__':
    unittest.main()