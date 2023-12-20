#!/usr/bin/python3
""" A class with update """


class Square:
    """Square stuff"""
    def __init__(self, size=0, position=(0, 0)):
        """assgin size"""
        self.__size = size
        """checking size type and value"""
    """Function to count area"""
    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        """The size property."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """The position property."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive ")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
