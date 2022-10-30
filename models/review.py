#!/usr/bin/python3
"""
Defines a class called Review that inherits
from the BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a Review object and inherits from
    a BaseModel class.
    """
    place_id = ""
    user_id = ""
    text = ""
