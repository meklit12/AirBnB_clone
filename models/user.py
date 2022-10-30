#!/usr/bin/python3
"""
Defines a User class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user object and inherits from
    the BaseModel class.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
