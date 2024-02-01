#!/usr/bin/python3
import uuid


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())