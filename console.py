#!/usr/bin/python3

import cmd, sys

class Hosh(cmd.Cmd):
    prompt = "(hbnb) "
    file = None

    def do_quit(self, arg):
        """ Quit the current hnbnb shell session"""
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


if __name__ == "__main__":
    Hosh().cmdloop()
