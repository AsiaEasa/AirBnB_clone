#!/usr/bin/python3
""" This is the MODELS for Place

"""


from models._im import *


class Place(BaseModel):
    """ The class Place to handel placese
    """

    "The attribute to this calss"
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
