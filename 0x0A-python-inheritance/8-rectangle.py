#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""A rectangel class"""


class Rectangle(BaseGeometry):
    """A rectangle instance"""

    def __init__(self, width, height):
        """Rectanle initialised"""

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
