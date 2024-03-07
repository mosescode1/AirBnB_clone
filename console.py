#!/usr/bin/python3
""" The command line interpreter """
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def do_EOF(self, line):
        """ go to a new line"""
        print()
        return True

    def do_quit(self, line):
        """Exit the program"""
        sys.exit()

    def emptyline(self):
        """Do nothing when and empty line is met"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
