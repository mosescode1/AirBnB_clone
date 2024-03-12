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

    def do_count(self, line):
        """Count the instance Created"""
        count = 0
        for key in storage.all():
            args = key.split(".")
            if line == args[0]:
                # if value["__class__"] == line:
                count += 1
        print(count)

    def default(self, line: str) -> None:
        """Default Argument passed to the cmdline"""
        # splits the command line argument
        args = line.split(".")
        # Checks if the arg[0] is in the file storage and if args[1] ends with

        # all Available Instance
        class_names = ['User', 'BaseModel',
                       "Place", "City", "Amenity", "State",
                       "Review"
                       ]

        # prints all the instance based on the class name
        if args[0] in class_names and args[1].endswith("all()"):
            self.do_all(args[0])
        # counting the instance based on the class
        elif args[0] in class_names and args[1].endswith("count()"):
            self.do_count(args[0])
        elif args[0] in class_names and args[1].startswith("show"):
            # show a dictionary representation based on the id passed
            striped = args[1].strip("show(\"").strip("\")")
            key = "{}.{}".format(args[0], striped)
            if key not in storage.all():
                print('** no instance found **')
                return
            print(storage.all()[key])

        elif args[0] in class_names and args[1].startswith("destroy"):
            # delete an instance based on the id passed
            striped = args[1].strip("destroy(\"").strip("\")")
            key = "{}.{}".format(args[0], striped)
            if key not in storage.all():
                print('** no instance found **')
            del storage.all()[key]
            storage.save()

        elif args[0] in class_names and args[1].startswith("update"):
            striped = args[1].strip("update(\"").strip("\)")
            stripped_value = striped.split(",")

            # checks if it meets all expectations
            if len(stripped_value) < 3:
                print("** value missing **")
                return

            # stripped class_id, class_key, class_attr
            class_id = stripped_value[0].strip("\"")
            class_key = stripped_value[1]
            class_attr = stripped_value[2]

            key = "{}.{}".format(args[0], class_id)
            if key not in storage.all():
                print('** no instance found **')
                return

            attribute_value = None
            attr_key = None

            try:
                attribute_value = eval(class_attr)
                attr_key = eval(class_key)
                setattr(storage.all()[key], attr_key, attribute_value)
            except Exception as e:
                print("** value missing **")
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
