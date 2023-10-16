#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define class Base"""
import json


class Base:
    """Represent Base class.

    Attributes:
        __nb_objects (int): private class attribute that icreaments only if
        id is None, Ensures unique id for each instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer.

        Args:
            id (int): public instance attribute.
            if id is not None assign id with the value
            otherwise increament private class attribute __nb_instances and
            assign to id it value.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json representation of list_dictionaries.

        Args:
            list_dictionaries (object): list of dictionaries
        Return:
            Json representation of list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json string representation to file.

        Args:
            list_objs (objects): list of instances who inherit of Base.
        """
        filename = "{:s}.json".format(cls.__name__)
        with open(filename, mode='w', encoding='utf-8') as fp:
            if list_objs is None or len(list_objs) < 1:
                fp.write("[]")
            list_dicts = [cls.to_dictionary() for cls in list_objs]
            fp.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of json string representation.

        Args:
            json_string (list of dictionaries): parameter
        Return:
            empty list if json_string is None or empty
            otherwise list represnted by json
        """
        if json_string is None or len(json_string) < 1:
            return []
        json_dict = json.loads(json_string)
        return list(json_dict)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary (pointer): to dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_class = cls(10, 10)
            else:
                new_class = cls(10)
            new_class.update(**dictionary)
            return new_class

    @classmethod
    def load_from_file(cls):
        """returns a list of instances."""
        filename = '{:s}.json'.format(cls.__name__)
        try:
            with open(filename, "r", encoding='utf-8') as a_file:
                list_dicts = Base.from_json_string(a_file.read())
            return [cls.create(**obj) for obj in list_dicts]
        except (FileNotFoundError, IOError):
            return []
