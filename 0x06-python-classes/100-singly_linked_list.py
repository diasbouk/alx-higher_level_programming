#!/usr/bin/python3
"""Class representing a Node"""


class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
    @property
    def data(self):
        """The data property."""
        return self.__data
    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The next_node property."""
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if value != None or type(value) is not list:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Singly Linked_list class"""
class SinglyLinkedList:
    def __init__(self, head=None):
        self.__head = head
    def sorted_insert(self, value):
        self.__value = value
