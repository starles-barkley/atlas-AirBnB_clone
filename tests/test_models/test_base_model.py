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
        expected_output = f"[{type(self.my_model).__name__}] ({self.my_model.id}) ({self.my_model.__dict__})"
        self.assertEqual(str(self.my_model), expected_output)

    def test_save(self):
        