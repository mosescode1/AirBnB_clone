#!/usr/bin/python3
""" File Storage Module """
import json
from datetime import datetime


class FileStorage:
    """ Class for Serlization and deserilization """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ Retuns the dictionary of file storage"""
        return self.__objects

    def new(self, obj):
        """ create a new dictionary"""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ Serizize a python dictionary to a
        file
        """
        objects = {}
        for key, value in self.__objects.items():
            objects[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(objects, file)

    def reload(self):
        """ Relaod the json file to python dictionary """
        from models.base_model import BaseModel
        definedclass = {'BaseModel': BaseModel}
        try:
            with open(self.__file_path) as file:
                content = file.read()
                if content:
                    loaded_content = json.loads(content)
                    for value in loaded_content.values():
                        class_name = value['__class__']
                        class_obj = definedclass[class_name]
                        self.new(class_obj(**value))
        except FileNotFoundError:
            pass
