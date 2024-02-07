#!/usr/bin/python3
""" class Amenity inherits from Base Model
stores name of amenity
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """ defines amenity instance with public attribute"""
    name = ""
