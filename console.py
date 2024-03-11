#!/usr/bin/python3
""" The command line interpreter """
import cmd
import sys
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """ The console for navigating through the
        Airbnb
    """
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

        # copy everthung in doshow exoect thebprint
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

    def do_update(self, line):
        """Updates the instance of Json based on the
        class name and id

        args:
            (line): command line argument passed
        """

        # splits the command line into a list
        args = line.split()

        # checks if the class name is passed to the cmd interpreter
        if len(args) < 1:
            print("** class name missing **")
            return

        # gets the value of the first argument
        # and checks if class name exists
        class_name = args[0]
        if class_name not in FileStorage.definedclass:
            print("** class doesn't exist **")
            return

        # checks if id is being passed
        if len(args) < 2:
            print("** instance id missing **")
            return

        # checks if the id exist
        class_id = args[1]
        key = f"{class_name}.{class_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        class_key = args[2]
        class_value = args[3]

        attribute_value = None

        try:
            attribute_value = eval(class_value)
            setattr(storage.all()[key], class_key, attribute_value)
        except Exception as e:
            print("** value missing **")

        storage.save()

    def default(self, line: str) -> None:
        # splits the command line argument
        args = line.split(".")
        """Checks if the arg[0] is in the file storage"""
        if args[0] in ['User', 'BaseModel',
                       "Place", "City", "Amenity", "State",
                       "Review"
                       ]:
            self.do_all(args[0])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
