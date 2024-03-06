#!/usr/bin/python3
""" BaseModel module for subclasses"""
import uuid
import datetime


class BaseModel:
    """
        base model class
    """

    def __init__(self):
        """ initilizing the base model """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ Returns a string representation of base model """
        mod_name = self.__class__.__name__
        string = "[{}] ({}) {}".format(mod_name, self.id, self.__dict__)
        return string

    def save(self):
        """ update the current datetime """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary representation of base model """
        base_model_dict = self.__dict__
        base_model_dict['__class__'] = self.__class__.__name__
        for key, value in base_model_dict.items():
            if key in ['updated_at', 'created_at']:
                base_model_dict[key] = value.isoformat()
        return base_model_dict
