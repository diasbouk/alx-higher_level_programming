#!/usr/bin/python3

""" Docs for modules and stuff """
import json


class Base:
    """ The base class for our project """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        if list_objs is None:
            return []
        else:
            list_objs = [inst.to_dictionary() for inst in list_objs]
            with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as file:
                file.write(cls.to_json_string(list_objs))
