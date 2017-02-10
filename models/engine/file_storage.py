#!/usr/bin/python3

import json

class FileStorage:
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        objects = {}
        for key in self.__objects.keys():
            objects[key] = self.__objects[key].to_json()
        with open(self.__file_path, 'w') as file:
            json.dump(objects, file)

    def reload(self):
        try:
            from ..base_model import BaseModel
            objects = {}
            with open(self.__file_path, 'r') as file:
                objects = json.load(file)
                for key in objects.keys():
                    self.__objects[key] = BaseModel(objects[key])
        except FileNotFoundError:
            pass
