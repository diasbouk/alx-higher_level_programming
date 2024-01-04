#!/usr/bin/python3

"""
Rectangle class
"""


class Rectangle:

    """
    Nothing goes
    here
    """
    def __init__(self, width=0, height=0):
        # Assigning attributes
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        wdith getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            self: obj to assign
            value: value to set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.stter
    def hieght(self, value):
        """
        Args:
            value: value to assign
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
