#!/usr/bin/python3
"""Module for User Profile"""

from models.base_model import BaseModel


class User(BaseModel):
    """_User class inherites from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
