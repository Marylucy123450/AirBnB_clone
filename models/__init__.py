#!/usr/bin/python3
"""
Package: models
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity

from os import environ

dummy_classes = {"BaseModel": BaseModel,
                 "User": User,
                 "Review": Review,
                 "City": City,
                 "State": State,
                 "Place": Place,
                 "Amenity": Amenity}