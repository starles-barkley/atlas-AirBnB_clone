import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def test_all_method(self):
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method(self):
        my_model = BaseModel()
        self.storage.new(my_model)
        self.assertIn('BaseModel.{}'.format(my_model.id), self.storage.all())

    def test_save_method(self):
        # Check if save method writes to file
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()

        # Read the file and check if the object is saved
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
            self.assertIn('BaseModel.{}'.format(my_model.id), data)

    def test_reload_method(self):
        # Ensure reload method loads objects from file
        my_model = BaseModel()
        my_model.name = "Test Model"
        self.storage.new(my_model)
        self.storage.save()

        # Clear __objects and reload from file
        self.storage.__objects = {}
        self.storage.reload()

        # Check if the reloaded object is present
        self.assertIn('BaseModel.{}'.format(my_model.id), self.storage.all())

    def test_save_and_reload_methods(self):
        # Create an instance of BaseModel and add it to storage
        my_model = BaseModel()
        self.storage.new(my_model)

        # Save the objects to the file
        with patch('builtins.input', return_value='yes'):
            self.storage.save()

        # Clear the objects from storage
        self.storage.__objects = {}

        # Reload the objects from the file
        self.storage.reload()

        # Check if the reloaded object is present
        self.assertIn('BaseModel.{}'.format(my_model.id), self.storage.all())

if __name__ == '__main__':
    unittest.main()
