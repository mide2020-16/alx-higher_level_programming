#!/usr/bin/python3
""" Defines a class square"""


class Square:
    """A class called Square that creates a square"""

    def __init__(self, size=0):
        """An initialization of the class Square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    def area(self):
        """Calculates the area of a Square"""

        return self.__size ** 2

