#!/usr/bin/python3

""" Modules and imports stuff goes here """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Representing a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """String repesenting of the class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """The size property."""
        return self.width

    @size.setter
    def size(self, value):
        self.width= value
        self.height= value

    def update(self, *args, **kwargs):
        """ Updates the class """
        if args:
            if args[0] is not None:
                self.id = args[0]
            if args[1] is not None:
                self.size = args[1] 
            if args[2] is not None:
                self.x = args[2]
            if args[3] is not None:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                self.key = value
