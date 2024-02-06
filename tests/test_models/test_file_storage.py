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