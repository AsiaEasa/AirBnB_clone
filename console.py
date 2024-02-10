#!/usr/bin/python3
""" Module to Console

"""

from imports import *


class HBNBCommand(cmd.Cmd):
    """Command interpreter class.
    """

    "The attribute to this class"
    prompt = "(hbnb) "
    KH = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }
    KH_K = list(KH.keys())

    def default(self, arg):
        """the default method of the parent class.
        """

        " Make the app work non-interactively"
        if not sys.stdin.isatty():
            print()

        args = arg.split(".")
        C_name = args[0]
        " Check if the line matches the pattern <class name>.all()"
        A = re.search(r"^(\w*)\.all\(\)$", arg)
        if A:
            self.do_all(C_name)
            return ""

        " Check if the line matches the pattern <class name>.count()"
        B = re.search(r"^(\w*)\.count\(\)$", arg)
        if B:
            self.do_count(C_name)
            return ""

        " Check if the line matches the pattern <class name>.show(<id>)"
        C = re.search(r"^(\w*)\.show\(['\"]?([\w-]+)['\"]?\)$", arg)
        if C:
            ID = args[1][5:-1]
            Input = f"{C_name} {ID}"
            self.do_show(Input)
            return ""

        " Check if the line matches the pattern <class name>.destroy(<id>)"
        D = re.search(r"^(\w*)\.destroy\(['\"]?([\w-]+)['\"]?\)$", arg)
        if D:
            ID = args[1][8:-1]
            Input = f"{C_name} {ID}"
            self.do_destroy(Input)
            return ""

        " Check if the line matches the pattern of update in 15 and 16"
        X = re.search(
            r"^(\w*)\.update\(['\"]?([\w-]+)['\"]?, "
            r"['\"]?([\w-]+)['\"]?, (.*?)\)$",
            arg
        )

        Y = re.search(
            r"^(\w+)\.update\(['\"]?([\w-]+)['\"]?, ({.*})\)$",
            arg
        )

        if X:
            PR = args[1][7:-1]
            AR = PR.split(", ")
            Input = f"{C_name} {AR[0]} {AR[1]} {AR[2]}"
            self.do_update(Input)
            return ""

        if Y:
            PR = args[1][7:-1]
            AR = PR.split(", ", 1)
            ID = AR[0]
            QU = AR[1].replace("'", '"')
            SS = json.loads(QU)
            for K in SS:
                V = SS[K]
                Input = f"{C_name} {ID} {K} {V}"
                self.do_update(Input)
            return ""

        if not A and not B and not C and not D and not X and not Y:
            print("*** Unknown syntax: {}".format(arg))

    def do_all(self, arg):
        """Prints string representation of all instances or to any class.
        """

        "spilt the argment"
        args = shlex.split(arg)
        if not args:
            ALL_inst = [str(V) for V in models.storage.all().values()]
            print(ALL_inst)
        elif args[0] not in HBNBCommand.KH_K:
            print("** class doesn't exist **")
        else:
            ALL_ins = [
                str(V)
                for K, V in models.storage.all().items()
                if type(V).__name__ == args[0]
            ]
            print(ALL_ins)

    def do_create(self, arg):
        """Create a new instance of classes, save it, and print the id.
        """

        if not arg:
            print("** class name missing **")
        else:
            if arg not in HBNBCommand.KH_K:
                print("** class doesn't exist **")
            else:
                _CLASS = self.KH.get(arg)
                New_in = _CLASS()
                models.storage.save()
                print(New_in.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        """

        " spilt the argment"
        args = shlex.split(arg)
        if not args or len(args) < 1:
            print("** class name missing **")
        else:
            if args[0] not in HBNBCommand.KH_K:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                inst_key = f"{args[0]}.{args[1]}"
                if inst_key in models.storage.all():
                    print(models.storage.all()[inst_key])
                else:
                    print("** no instance found **")
        return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        """

        "spilt the argmemt"
        args = shlex.split(arg)
        if not args or len(args) < 1:
            print("** class name missing **")
            return
        else:
            if args[0] not in HBNBCommand.KH_K:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
                return
            else:
                inst_key = f"{args[0]}.{args[1]}"
                if inst_key in models.storage.all():
                    del models.storage.all()[inst_key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id.
        """

        " split the argment"
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.KH_K:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            ins_K = f"{args[0]}.{args[1]}"
            if ins_K not in models.storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                OB = models.storage.all()[ins_K]
                try:
                    t = type(getattr(OB, args[2]))
                    args[3] = t(args[3])
                except AttributeError:
                    pass
                setattr(OB, args[2], args[3])
                models.storage.save()

    def do_count(self, arg):
        """retrieve the number of instances of a class.
        """

        " split the argment"
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.KH_K:
            print("** class doesn't exist **")
        else:
            "variable to use in count"
            C = 0
            for K in models.storage.all().keys():
                class_name, instance_id = K.split(".")
                if args[0] == class_name:
                    C += 1
            print(C)

    def do_quit(self, arg):
        """Quit command to exit the program.
        """

        return True

    def do_EOF(self, arg):
        """EOF command to exit the program.
        """

        print()
        return True

    def emptyline(self):
        """Do nothing on empty line.
        """

        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
