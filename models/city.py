#!/usr/bin/python3
""" module for City subclass of BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """ initiate instance of City subclass,
    with public attributes
    """
    state_id = ""
    name = ""
