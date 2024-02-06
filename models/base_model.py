#!/usr/bin/python3
"""
define BaseModel class that defines attributes/methods
"""
import uuid
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.engine.file_storage import FileStorage

class BaseModel:
    """
    basemodel class defines methods and attributes for subclasses
    """
    def __init__(self, *args, **kwargs):
        """ conductor method for initializing instances """
        from models import storage
        formatted = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key in kwargs:
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(kwargs[key], formatted))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ print string representation of created object """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        from models import storage
        storage.save()

    def to_dict(self): 
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict