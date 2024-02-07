#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):

    def setUp(self):
        self.my_state = State()

    def test_attributes_initialization(self):
        self.assertEqual(self.my_state.name, "")

if __name__ == '__main__':
    unittest.main()