#!/usr/bin/python3
""" MODELS to USER

"""

from models._im import *


class User(BaseModel):
    """ The USER that will inhereit from the base
    """

    "The attribute to this calss"
    email = ""
    password = ""
    first_name = ""
    last_name = ""
