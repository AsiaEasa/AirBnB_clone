#!/usr/bin/python3
""" MODELS to Review

"""

from models._im import *


class Review(BaseModel):
    """ Class of REVIEWS
    """

    "The attribute to this calss"
    place_id = ""
    user_id = ""
    text = ""
