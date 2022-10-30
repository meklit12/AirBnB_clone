#!/usr/bin/python3
"""
Defines a class called Amenity that inherits
from the BaseModel class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an Amenity object and inherits from
    a BaseModel class.
    """
    name = ""
