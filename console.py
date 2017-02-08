#!/usr/bin/python3


import cmd

class MyConsole(cmd.Cmd):

    prompt = '(hnbb)'
    
    undoc_header = 'Documented commands (type help <topic>):'
 
    ruler = '='
    
    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Exits'
        return True


if __name__ == '__main__':
    MyConsole().cmdloop()
