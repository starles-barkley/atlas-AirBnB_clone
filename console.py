#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        return True

if __name__ == '_main__':
    HBNBCommand().cmdloop()