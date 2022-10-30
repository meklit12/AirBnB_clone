#!/usr/bin/python3
"""
Defines a class called City that inherits
from the BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a City object and inherits from
    a BaseModel class.
    """
    state_id = ""
    name = ""
