#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
            print('\r')
            return True

    def help_quit(self):
        print("Exit the interpreter")

if __name__ == '_main__':
    HBNBCommand().cmdloop()