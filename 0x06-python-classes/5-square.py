#!/usr/bin/python3
""" Defines a class square"""


class Square:
    """A class called Square that creates a square"""

    def __init__(self, size=0):
        """An initialization of the class Square"""

        self.__size = size

    @property
    def size(self):
        """Gets a pivate attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets a private atribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of a Square"""

        return self.__size**2

    def my_print(self):
        """Prints a square with #"""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print(self.__size * "#")
