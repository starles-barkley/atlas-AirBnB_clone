#!/usr/bin/python3

import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        self.my_review = Review()

    def test_attributes_initialization(self):
        self.assertEqual(self.my_review.name, "")

if __name__ == '__main__':
    unittest.main()