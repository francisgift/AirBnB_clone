#!/usr/bin/python3
'''class inherent BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''class amenity'''

    name = ""

    def __init__(self, *args, **kwargs):
        """initialize Amenity"""
        super().__init__(*args, **kwargs)
