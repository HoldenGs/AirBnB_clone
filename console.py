#!/usr/bin/python3

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class Hosh(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Review", "Place"]
    file = None

    def preloop(self):
        self.create_class_methods()

    def do_update(self, arg):
        """Update or create a new attribute for an object"""
        obj = find_object(self, arg)
        if obj is None:
            return
        args = arg.split(' ')
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(obj, args[2], args[3].strip('"'))
        obj.save()

    def do_all(self, arg):
        """Print all objects stored"""
        if len(arg) == 0:
            for key in storage.all().keys():
                print(storage.all()[key])
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        for key in storage.all().keys():
            if storage.all()[key].__class__.__name__ == arg:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an object"""
        obj = find_object(self, arg)
        if obj is not None:
            del storage.all()[obj.id]
            storage.save()

    def do_show(self, arg):
        """Print out an object"""
        obj = find_object(self, arg)
        if obj is not None:
            print(obj)

    def do_create(self, arg):
        """Create a new BaseModel object"""
        if arg == "BaseModel":
            new_model = BaseModel()
        elif arg == "User":
            new_model = User()
        elif arg == "State":
            new_model = State()
        elif arg == "City":
            new_model = City()
        elif arg == "Amenity":
            new_model = Amenity()
        elif arg == "Place":
            new_model = Place()
        elif arg == "Review":
            new_model = Review()
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

    def create_class_methods(self):
        """Create a do_<cls> method for each existing class"""
        for cls in self.classes:
            self.create_method(cls)

    def create_method(self, cls):
        """Create a do_<cls> method for a class"""
        def class_method(self, arg):
            """Parses arg line and formats a string to use existing methods"""
            args = arg.split('(')
            if args[0][:1] == '.' and args[1][-1:] == ')':
                formatted_arg = class_method.__name__[3:] + " " + args[1][:-1]
                l = formatted_arg.split(' ')
                value = ''
                if len(l) > 4:
                    print("too many arguments")
                    return
                if len(l) > 3:
                    value = l[3].replace("'", '"')
                if len(l) > 1:
                    formatted_arg = ""
                    for item in l[:-1]:
                        formatted_arg += " " + item.strip(',')
                formatted_arg = formatted_arg + " " + value
                formatted_arg = formatted_arg.strip(' ')
                exec("self.do_{:s}('{:s}')".format(args[0][1:], formatted_arg))
        docstring = "Execute method for {} based on argument".format(cls)
        class_method.__doc__ = docstring
        class_method.__name__ = "do_{}".format(cls)
        setattr(self.__class__, class_method.__name__, class_method)

    def close(self):
        """Close any open file before exiting"""
        if self.file:
            self.file.close()
            self.file = None


def find_object(self, arg):
    """Find an object based on class and id"""
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
