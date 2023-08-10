#!/usr/bin/python3
'''A class user that inherit from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''represent User class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
