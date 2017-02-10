#!/usr/bin/python3

import cmd, sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage

class Hosh(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel"]
    file = None

    def do_destroy(self, arg):
        """Delete an object"""
        obj = find_object(self, arg)
        if obj != None:
            del storage.all()[obj.id]

    def do_show(self, arg):
        """Print out an object"""
        obj = find_object(self, arg)
        if obj != None:
            print(obj)

    def do_create(self, arg):
        """Create a new BaseModel object"""
        if arg == "BaseModel":
            new_model = BaseModel()
            new_model.save()
            print("{}".format(new_model.id))

    def do_quit(self, arg):
        """Quit the current hbnb shell session"""
        self.close()
        return True

    def do_EOF(self, arg):
        """Quit the current hbnb shell session"""
        print()
        self.close()
        return True

    def emptyline(self):
        """Do nothing when entered an empty line"""
        pass

    def close(self):
        """Close any open file before exiting"""
        if self.file:
            self.file.close()
            self.file = None

def find_object(self, arg):
    if len(arg) == 0:
        print("** class name missing **")
        return None
    args = arg.split(' ')
    if len(args) < 2:
        print("** instance id missing **")
        return None
    if args[0] not in self.classes:
        print("** class doesn't exist **")
        return None
    stored_objects = storage.all()
    for object_id in stored_objects.keys():
        if object_id == args[1]:
            return stored_objects[object_id]
    print("** no instance found **")
    return None

if __name__ == "__main__":
    Hosh().cmdloop()
