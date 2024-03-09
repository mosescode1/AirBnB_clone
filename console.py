#!/usr/bin/python3
""" The command line interpreter """
import cmd
import sys
from models.engine.file_storage import FileStorage
from models import storage


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

    def do_create(self, line):
        """ creates new instance based on the class passed """
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        class_name = args[0]
        if class_name not in FileStorage.definedclass:
            print('** class name doesn\'t exist **')
            return
        else:
            instanceNew = FileStorage.definedclass[args[0]]()
            instanceNew.save()
            print(instanceNew.id)

    def do_show(self, line):
        """ prints the strings representation """
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        class_name = args[0]
        if class_name not in FileStorage.definedclass:
            print('** class name doesn\'t exist **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        instanceId = args[1]
        key = "{}.{}".format(class_name, instanceId)
        if key not in storage.all():
            print('** no instance found **')
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """ Delete and instance dictuonary """

        #copy everthung in doshow exoect thebprint

        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """ Print all the instance """
        args = line.split()
        if not args:
            print([str(value) for value in storage.all().values()])
            return
        class_name = args[0]

        if class_name not in FileStorage.definedclass:
            print('** class doesn\'t exist **')
        else:
            list_obj = []
            for value in storage.all().values():
                if value.__class__.__name__ == class_name:
                    list_obj.append(str(value))
            print(list_obj)




        

        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
