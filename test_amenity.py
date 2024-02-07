#!/usr/bin/python3

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.my_amenity = Amenity()

    def test_attributes_initialization(self):
        self.assertEqual(self.my_amenity.name, "")

if __name__ == '__main__':
    unittest.main()