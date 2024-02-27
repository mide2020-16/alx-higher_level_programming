#!/usr/bin/python3
"""
Base Class for Geometric shapes
"""
import json
from models.rectangle import Rectangle
from models.square import Square



class Base:
    """Base class for geometric shapes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an optional ID."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serialize a list of dictionaries into a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representing the list of dictionaries.
        """

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to be saved.
        """

        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"

        with open(filename, 'w') as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a JSON string into a list of dictionaries.

        Args:
            json_string (str): JSON string to be deserialized.

        Returns:
            list: List of dictionaries.
        """

        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of a class using a dictionary.

        Args:
            **dictionary: Dictionary containing attributes of the instance.

        Returns:
            object: Instance of the class.
        """

        if cls.__name__ == 'Rectangle':
            dum_instance = Rectangle(1, 1)
        elif cls.__name__ == 'Square':
            dum_instance = Square(1)
        else:
            raise ValueError("Unsupported Geometry")

        dum_instance.update(**dictionary)
        return dum_instance

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file and return a list of instances.

        Returns:
            list: List of instances loaded from the file.
        """

        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for dictionary in dictionaries]
                return instances

        except FileNotFoundError:
            return []
