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
        """Default behavior for cmd module when input is invalid"""

        TT = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count,
        }
        match = re.search(r"\.", arg)
        if bool(match):
            arg_list = arg.split(".")
            clsS = arg_list[0]
            start, end = match.span()
            arGl = [arg[:start], arg[end:]]

            match = re.search(r"\((.*?)\)", arGl[1])
            if bool(match):
                start, end = match.span()
                command = arg_list[1].split("(")
                cmet = command[0]
                e_arg = command[1].split(")")[0]
                al = e_arg.split(",")
                cotext = arGl[1][:start]
                coarg = match.group()[1:-1]
                command = [cotext, coarg]

                if cmet in TT.keys():
                    if cmet != "update":
                        call = f"{arGl[0]} {e_arg}"
                        return TT[cmet](call)
                    elif len(al) >= 2 and re.search(r"\{.*?\}", e_arg):
                        ob = al[0]
                        ana = al[1:]
                        ana[0] = ana[0].lstrip()
                        for i in range(1, len(ana)):
                            ana[i] = "," + ana[i]
                        jostr = "".join(ana)
                        result_dict = ast.literal_eval(jostr)
                        for k, v in result_dict.items():
                            TT[cmet]("{} {} {} {}".format(clsS, ob, k, v))
                        return ""

                    elif len(al) == 3:
                        ob = al[0]
                        ana = al[1:]
                        for i in range(0, len(ana)):
                            ana[i] = ana[i].lstrip()
                            TT[cmet](
                                "{} {} {} {}".format(clsS, ob, ana[0], ana[1])
                            )
                        return ""

        print(f"*** Unknown syntax: {arg}")

        return False

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
