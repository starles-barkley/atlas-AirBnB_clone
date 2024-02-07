#!/usr/bin/python3


"""module for file storage engine,
includes JSON handling methods
"""
import json
import os
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.base_model import BaseModel


class FileStorage:
    """ class for serializing and deserializing with JSON """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary of objects """
        return self.__objects

    def new(self, obj):
        """ method adds object to dictionary """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ save instances - serialization """
        with open(self.__file_path, 'w') as file:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """ reload instance - deserialization"""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass