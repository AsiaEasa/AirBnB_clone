#!/usr/bin/python3
"""MODELS for STORE

"""


from models.engine.im import *


class FileStorage():
    """ A class FILESTORAGE to serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    "Private class attributes:"
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary
        """

        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """

        "To get the OBJ"
        K = obj.__class__.__name__
        ID = obj.id
        FileStorage.__objects[f"{K}.{ID}"] = obj

    def save(self):
        """ serializes __objects to the JSON file
        """

        "varible to get the dict"
        New = {K: V.to_dict() for K, V in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, 'w')as fi_1:
            json.dump(New, fi_1)

    def reload(self):
        """ deserializes the JSON file to __objects
        """

        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF8") as fi_2:
                LOAD = json.load(fi_2)
                for K in LOAD.keys():
                    "give value of key in dict"
                    V = LOAD[K]
                    classname = eval(V["__class__"])(**V)
                    FileStorage.__objects[K] = classname
        except FileNotFoundError:
            pass
