#!/usr/bin/python3
"""
Module: file_storage.py
"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

classes = {
    'BaseModel': BaseModel,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review,
    'User': User
}


class FileStorage:
    """
    Class to manage serialization and deserialization of instances
    to and from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        """
        Getter for the file path.

        Returns:
            str: File path.
        """
        return FileStorage.__file_path

    @property
    def objects(self):
        """
        Getter for the stored objects.

        Returns:
            dict: Dictionary containing stored objects.
        """
        return FileStorage.__objects

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or all objects of a specific class.

        Args:
            cls (class, optional): Class to filter objects.

        Returns:
            dict: Dictionary containing objects.
        """
        if cls:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        return self.__objects


    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (BaseModel): Object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes objects to JSON and saves to file.
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        Deserializes objects from JSON file and reloads into storage.
        Ignores FileNotFoundError.
        """
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                cls_name, obj_id = key.split('.')
                cls = classes[cls_name]
                FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
