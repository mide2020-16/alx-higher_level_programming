#!/usr/bin/python3
"""A square recreation and subclass example"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass and initialization

    Args:
        Rectangle (class): A rectangle class

    Return: void
    """
    def __init__(self, size):
        """Initialse square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area of a square"""

        return self.__size * self.__size
