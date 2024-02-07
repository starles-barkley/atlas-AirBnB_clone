#!/usr/bin/

"""module for Review subclass of BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """initiate Review subclass object """
    place_id = ""
    user_id = ""
    text = ""
