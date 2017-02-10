#!/usr/bin/python3

import json
import datetime

class FileStorage:
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file,
                      default=lambda obj:
                      (obj.isoformat() if isinstance(obj, datetime.datetime) else obj.__dict__))

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
