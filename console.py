#!/usr/bin/python3
""" module for python command line interpreter """
import cmd
import sys
import importlib
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """ class initiates command loop"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ quit method quits interpreter """
        exit()

    def do_EOF(self, arg):
            """end of file method exits interpreter"""
            print()
            exit()

    def emptyline(self):
         pass

    def help_quit(self):
        """ help message for quit method"""
        print("Exit the interpreter")

    def do_create(self, arg):
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            module = importlib.import_module('models.base_model')
            class_ = getattr(module, class_name)
            instance = class_()
            instance.save()
            print(instance.id)
        except AttributeError:
             print("** class doesn't exist **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()