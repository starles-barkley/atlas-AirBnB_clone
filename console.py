#!/usr/bin/python3
import cmd
""" module for python command line interpreter """
class HBNBCommand(cmd.Cmd):
    """ class initiates command loop"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ quit method quits interpreter """
        return True

    def do_EOF(self, arg):
            """end of file method exits interpreter"""
            print('\r')
            return True

    def help_quit(self):
        """ help message for quit method"""
        print("Exit the interpreter")

if __name__ == '_main__':
    HBNBCommand().cmdloop()