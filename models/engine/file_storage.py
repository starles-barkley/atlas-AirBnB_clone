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
        json_save = json.dumps(self.__objects)
        with open(self.__class__.__file_path, 'w') as file:
            file.write(json_save)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode = 'r') as file:
                self.__objects = json.load(file)