#!/usr/bin/python3
""" BaseModel module for subclasses"""
import uuid
from datetime import datetime
# from models import storage


class BaseModel:
    """
        base model class
    """

    def __init__(self, *args, **kwargs):
        """ initilizing the base model """
        if kwargs:
            for key in kwargs.keys():
                if key == 'created_at':
                    self.__dict__[key] = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # storage.new(self)

    def __str__(self):
        """ Returns a string representation of base model """
        mod_name = self.__class__.__name__
        string = "[{}] ({}) {}".format(mod_name, self.id, self.__dict__)
        return string

    def save(self):
        """ update the current datetime """
        from models import storage
        self.updated_at = datetime.utcnow()

        storage.new(self)
        storage.save()

    def to_dict(self):
        """ returns a dictionary representation of base model """
        base_model_dict = self.__dict__.copy()
        base_model_dict['__class__'] = self.__class__.__name__
        for key, value in base_model_dict.items():
            if key in ['updated_at', 'created_at']:
                base_model_dict[key] = value.isoformat()
        return base_model_dict
