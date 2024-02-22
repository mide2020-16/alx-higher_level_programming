#!/usr/bin/python3
"""
a class Student that defines a student
"""


class Student:
    """
    a class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """INitialse student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert to json dict"""
        if isinstance(attrs, list):
            return {attr:
                    getattr(self, attr)
                    for attr in attrs
                    if hasattr(self, attr)
                    }
        else:
            return self.__dict__
