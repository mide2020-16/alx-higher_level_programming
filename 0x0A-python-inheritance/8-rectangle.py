#!/usr/bin/python3
"""A rectangel class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle instance"""

    def __init__(self, width, height):
        """Rectanle initialised"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
