#!/usr/bin/python3

import json
from models import *

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
            objects = {}
            with open(self.__file_path, 'r') as file:
                objects = json.load(file)
                for key in objects.keys():
                    cls = objects[key].get('__class__')
                    if cls == "Review":
                        self.__objects[key] = Review(objects[key])
                    if cls == "Place":
                        self.__objects[key] = Place(objects[key])
                    if cls == "Amenity":
                        self.__objects[key] = Amenity(objects[key])
                    if cls == "City":
                        self.__objects[key] = City(objects[key])
                    if cls == "State":
                        self.__objects[key] = State(objects[key])
                    if cls == "User":
                        self.__objects[key] = User(objects[key])
                    if cls == "BaseModel":
                        self.__objects[key] = BaseModel(objects[key])
        except FileNotFoundError:
            pass
