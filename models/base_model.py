#!/usr/bin/python3
""" This script is the base

"""


from models.im import *


class BaseModel:
    """ Class BaseModel
    """

    "The INIT method"
    def __init__(self, *args, **kwargs):
        """ CON
        """

        "IOS attribute to use in iosformate"
        IOS = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs and kwargs != {}:
            for K, V in kwargs.items():
                if K == "created_at" or K == "updated_at":
                    self.__dict__[K] = datetime.strptime(V, IOS)
                else:
                    if K != "__class__":
                        setattr(self, K, V)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ UPDATE the public instance attribute updated_at
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ To handle print()
        """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """ Returns a dictionary containing all K/V
        """

        "varible use in update to the dictionary"
        dict_C = self.__dict__.copy()
        K = ["created_at", "updated_at"]
        for KEY, V in self.__dict__.items():
            if KEY in K:
                dict_C[KEY] = V.isoformat()
        dict_C['__class__'] = self.__class__.__name__
        return dict_C
