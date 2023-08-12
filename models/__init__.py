#!/usr/bin/python3
"""create a unique FileStorage instance for your app"""
from models.engine.file_storage import FileStorage

"""A variable storage,instance of FileStorage"""
storage = FileStorage()
storage.reload()
