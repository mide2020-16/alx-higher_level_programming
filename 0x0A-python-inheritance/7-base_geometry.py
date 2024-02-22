#!/usr/bin/python3

"""A class called base geometry"""


class BaseGeometry:
    """A base geometry"""

    def area(self):
        """Area of something"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

