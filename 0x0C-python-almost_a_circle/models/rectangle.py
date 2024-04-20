#!/usr/bin/python3
""" Imports and stuff here ==> """
from typing import Type
from models.base import Base


class Rectangle(Base):
    """ Class rep rectangle """


    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(id)
        self.width = width
        self.height= height
        self.x= x
        self.y= y

    @property
    def width(self):
        """The width property."""
        return self.__width
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The height property."""
        return self.__height
    @height.setter
    def height(self, value):
        if type(value) != int:
                raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The x property."""
        return self.__x
    @x.setter
    def x(self, value):
        if type(value) != int:
                raise TypeError("x must be an integer")
        if value < 0:
                raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """They property."""
        return self._y
    @y.setter
    def y(self, value):
        if type(value) != int:
                raise TypeError("y must be an integer")
        if value < 0:
                raise ValueError("y must be >= 0")
        self._y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ Displays rectangle area """
        for i in range(self.__height):
            for i in range(self.__width):
                print("#",end="")
            print("")

