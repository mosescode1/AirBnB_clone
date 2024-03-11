#!/usr/bin/python3
"""Module for Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class for Place"""

    city_id = None
    user_id = None
    name = None
    description = None
    number_rooms = None
    number_bathrooms = None
    max_guest = None
    price_by_night = None
    latitude = None
    longitude = None
    amenity_ids = None
