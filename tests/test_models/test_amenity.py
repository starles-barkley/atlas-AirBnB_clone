#!/usr/bin/python3

import unittest
import models

class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.my_amenity = models.amenity.Amenity()

    def test_attributes_initialization(self):
        self.assertEqual(self.my_amenity.name, "")
