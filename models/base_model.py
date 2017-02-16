#!/usr/bin/python3

import datetime
import uuid
import copy
import models


class BaseModel:
    """
    Base Model which defines basic functions/attributes
    that every model will need
    """
    def __init__(self, *args, **kwargs):
        """
        Loads the model if it already exists.
        Creates a new model if it doesn't already exist
        """
        if len(args) > 0:
            if type(args[0]) is dict:
                self.__dict__ = args[0]
                self.updated_at = datetime.datetime.strptime(
                    self.updated_at, "%Y-%m-%d %H:%M:%S.%f")
                self.created_at = datetime.datetime.strptime(
                    self.created_at, "%Y-%m-%d %H:%M:%S.%f")
                return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        models.storage.new(self)

    def __str__(self):
        """
        Returns a formatted string object that looks like so:
        [<class>] (<id>) {<object.__dict__>}
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Save the model to the storage instance
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_json(self):
        """
        Creates and returns a dictionary which is json serializable
        """
        new_dict = copy.copy(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = str(self.updated_at)
        new_dict['updated_at'] = str(self.created_at)
        return new_dict
