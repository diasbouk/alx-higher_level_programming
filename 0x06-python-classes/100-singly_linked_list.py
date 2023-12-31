#!/usr/bin/python3
"""Class representing a Node"""


class Node:
    """class Node"""
    def __init__(self, data, next_node=None):
        self.__data = data

    @property
    def data(self):
        """The data property."""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The next_node property."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Singly Linked_list class"""


class SinglyLinkedList:
    """singly ll"""
    def __init__(self):
        """Defines a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        tmp = self.__head
        add_start = False

        if not self.__head:
            self.__head = new
            new.next_node = None
        else:
            if value < self.__head.data:
                add_start = True
            while tmp.next_node and value > tmp.next_node.data\
                    and not add_start:
                tmp = tmp.next_node
            if not add_start:
                new.next_node = tmp.next_node
                tmp.next_node = new
            else:
                new.next_node = tmp
                self.__head = new
            new.data = value

    def __str__(self):
        s = ""
        current = self.__head

        while current:
            s += str(current.data) + '\n'
            current = current.next_node
        return s[: -1]
