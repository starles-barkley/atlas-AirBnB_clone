import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

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
        #Check if save method writes to file
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        
        #Read the file and check if object is saved
        with open(self.storage.__file_path, 'r') as file:
            data = json.load(file)
            self.assertIn('BaseModel.{}'format(my_model.id), data)
        