#!/usr/bin/python3
"""module documentation"""

import json


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation
           of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None or len(list_objs) == 0:
            json_string = '[]'
        else:
            # converting to json
            json_objs_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(json_objs_list)

        # write to the file
        file_name = '{}.json'.format(cls.__name__)

        with open(file_name, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            py_object = json.loads(json_string)
            return py_object

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(2, 2)
        elif cls.__name__ == "Square":
            dummy_instance = cls(2)

        dummy_instance.update(**dictionary)
        return dummy_instance
