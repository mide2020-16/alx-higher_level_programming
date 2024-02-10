#!/usr/bin/python3
""" Defines a class square"""


class Square:
    """A class called Square that creates a square"""

    def __init__(self, size=0, position=(0, 0)):
        """An initialization of the class Square"""

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Gets position in a Square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets a position witha a value as private"""

        if (
            (not isinstance(value, tuple))
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or not all(value[0] < 0 or value[1] < 0)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of a Square"""

        return self.__size**2

    def my_print(self):
        """Prints a square with #"""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.__size):
                print(self.position * " ")
                print(self.__position[0] * " " + self.__size * "#")
