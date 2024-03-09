#!/usr/bin/python3
"""
Module for the BaseModel class that defines common attributes/methods for
other classes.
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """
    BaseModel class that defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Unused positional arguments.
            **kwargs: Dictionary containing attribute names and values.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the
         current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
