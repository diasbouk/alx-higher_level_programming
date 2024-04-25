#!/usr/bin/python3
""" Imports and stuff here ==> """
from models.base import Base


class Rectangle(Base):
    """Class rep rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.y = y

    @property
    def width(self):
        """The width property."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """They property."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Displays rectangle area"""
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Overrrides the str repes of the class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method that updates instance attributes via */**args."""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates the the class"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)


    def to_dictionary(self):
        """To dict"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }
