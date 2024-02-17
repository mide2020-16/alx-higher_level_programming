#!/usr/bin/python3
"""Decclare a class Rectangle"""


class Rectangle:
    """A new class called Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialzation of class"""

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

    def area(self):
        """Area of a rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Perimeter of a Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation for Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ""
            for _ in range(self.__height):
                result += ("#" * self.__width + "\n")

            return result

    def __repr__(self):
        """Formal Representation of Rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"
