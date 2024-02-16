#!/usr/bin/python3
"""Decclare a class Rectangle"""


class Rectangle:
    """A new class called Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialzation of class"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width Getter"""

        return self.__width

    @width.setter
    def width(self, width):
        """Width Setter"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Height getter"""

        return self.__height

    @height.setter
    def height(self, height):
        """Height Setter"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
