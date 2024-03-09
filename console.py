#!/usr/bin/env python3
"""
Module: console.py
"""

import cmd
import models
from models import storage, dummy_classes


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it to JSON file."""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name = args[0]

            if class_name not in models.dummy_classes:
                print("** class doesn't exist **")
                return

            template = models.dummy_classes[class_name]
            new_instance = template()

            for pair in args[1:]:
                pair_split = pair.split("=")
                attribute_name = pair_split[0]

                if hasattr(new_instance, attribute_name):
                    attribute_value = pair_split[1]

                    if attribute_value.startswith('"'):
                        attribute_value = attribute_value.strip('"').replace("\\", "").replace("_", " ")
                    elif "." in attribute_value:
                        try:
                            attribute_value = float(attribute_value)
                        except ValueError:
                            continue
                    else:
                        try:
                            attribute_value = int(attribute_value)
                        except ValueError:
                            continue

                    setattr(new_instance, attribute_name, attribute_value)

            new_instance.save()
            print(new_instance.id)

        except Exception as e:
            print(str(e))
            print("** class doesn't exist **")
            models.storage.rollback()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in models.dummy_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])

        try:
            print(models.storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file)."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if class_name not in models.dummy_classes:
            print("** class doesn't exist **")
            return

        try:
            instance = models.storage.all()[key]
            del models.storage.all()[key]
            models.storage.save()
        except KeyError:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """Prints string representations of all instances."""
        result = []
        if arg:
            class_name = arg.split()[0]
            if class_name in models.dummy_classes:
                instances = models.storage.all(models.dummy_classes[class_name])
                result = [str(obj) for key, obj in instances.items() if key.startswith(class_name + '.')]
            else:
                print("** class doesn't exist **")
        else:
            result = [str(obj) for obj in models.storage.all().values()]

        if result:
            print(result)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if class_name not in models.dummy_classes:
            print("** class doesn't exist **")
            return

        try:
            instance = models.storage.all()[key]
        except KeyError:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3].strip('"')

        # Check if the attribute is updatable
        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** cannot update read-only attribute **")
            return

        # Update the attribute and save the instance
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
