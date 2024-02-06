import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_str__(self):
    expected_output = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
    actual_output = str(self.my_model)
    print("Expected:", expected_output)
    print("Actual  :", actual_output)
    self.assertEqual(actual_output, expected_output)
