#!/usr/bin/python3
import json
import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.base_model import BaseModel

class FileStorage:
    """ class for serializing and deserializing with JSON """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ public instance method returns dictionary """
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
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