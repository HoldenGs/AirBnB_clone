#!/usr/bin/python3

import json
from models import *


class FileStorage:
    """
    This class makes a file to store json objects; it can serialize
    and deserialize json
    """
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """
        Returns the objects stored
        """
        return self.__objects

    def new(self, obj):
        """
        Instantiates a new file storage object that we can then use for storage
        """
        self.__objects[obj.id] = obj

    def save(self):
        """
        Serializes the objects as json and stores them in a file
        """
        objects = {}
        for key in self.__objects.keys():
            objects[key] = self.__objects[key].to_json()
        with open(self.__file_path, 'w') as file:
            json.dump(objects, file)

    def reload(self):
        """
        Deserializes the json string in the file and puts the objects
        in a dictionary
        """
        try:
            objects = {}
            with open(self.__file_path, 'r') as file:
                objects = json.load(file)
                for key, obj in objects.items():
                    self.__objects[key] = eval(obj['__class__'])(obj)
        except FileNotFoundError:
            pass
