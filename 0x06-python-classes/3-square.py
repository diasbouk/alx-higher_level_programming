#!/usr/bin/python3
""" A class with update """


class Square:
    """Square stuff"""
    def __init__(self, size=0):
        """assgin size"""
        self.__size = size
        """checking size type and value"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    """Function to count area"""
    def area(self):
        return self.__size * self.__size
