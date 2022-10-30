#!/usr/bin/python3
"""
Defines a class called State that inherits
from the BaseModel class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state object and inherits from
    a BaseModel class.
    """
    name = ""
