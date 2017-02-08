#!/usr/bin/python3


import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(hnbb)'
    intro = "a custom prompt"

    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'
    
    ruler = '-'
    
    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
