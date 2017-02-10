#!/usr/bin/python3

import datetime
import uuid
import copy
from . import storage

class BaseModel:

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            if type(args[0]) is dict:
                self.__dict__ = args[0]
                self.updated_at = datetime.datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
                self.created_at = datetime.datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
                return;
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_json(self):
        self.updated_at = datetime.datetime.isoformat(self.updated_at)
        self.created_at = datetime.datetime.isoformat(self.created_at)
        new_dict = copy.copy(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
