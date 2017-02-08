#!/usr/bin/python3

import datetime
import uuid
import copy

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now())

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        self.updated_at = str(datetime.datetime.now())

    def to_json(self):
        new_dict = copy.copy(self.__dict__)
        new_dict['__class__'] = 'BaseModel'
        return new_dict
