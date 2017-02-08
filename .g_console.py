#!/usr/bin/python3


import cmd

class MyConsole(cmd.Cmd):

    prompt = '(hnbb)'
    """
    intro = "a custom prompt"
    """
    
    doc_header = 'Documented commands (type help <topic>):'
    """
    misc_header = 'misc_header'
    """
    """
    undoc_header = 'undoc_header'
    """
    ruler = '='
    
    def do_quit(self, line):
        "Quit command to exit the program"
        self.prompt = line + ': '
    """
    def do_EOF(self, line):
        return True
    """

if __name__ == '__main__':
    MyConsole().cmdloop()
