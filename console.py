#!/usr/bin/python3
""" module for python command line interpreter """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """ class initiates command loop"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ quit method quits interpreter """
        exit()

    def do_EOF(self, arg):
            """end of file method exits interpreter"""
            print()
            exit()

    def help_quit(self):
        """ help message for quit method"""
        print("Exit the interpreter")

if __name__ == '_main__':
    HBNBCommand().cmdloop()