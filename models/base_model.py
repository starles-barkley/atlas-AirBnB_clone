#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.class_name = self.__class__.__name__

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.class_name, self.id, self.__dict__)

    def save(self):
        return self.updated_at

    def to_dict(self):
        
        dummy_dict = {
            self.__class__.__name__: {
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
            }
        }
        return dummy_dict