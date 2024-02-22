#!/usr/bin/python3
"""A rectangel class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle instance"""

    def __init__(self, width, height):
        """Rectanle initialised"""

        super().__init__()

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Area of a rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """String formalisasstion"""

        return f"[Rectangle] {self.__width}/{self.__height}"
