#!/usr/bin/python3
"""
A rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle's position.
        y (int): y-coordinate of the rectangle's position.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's position
            y (int, optional): y-coordinate of the rectangle's position
            id (int, optional): ID of the rectangle. Defaults to None.
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def to_dictionary(self):
        """
        Convert Rectangle attributes to a dictionary.

        Returns:
            dict: Dictionary containing attributes of the Rectangle.
        """

        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """

        return self.__width * self.__height

    def display(self):
        """Display the rectangle."""

        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Update attributes with keyword arguments or positional arguments.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """

        if args:
            self.id = args[0]
            args = args[1:]

        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value

    def __str__(self):
        """
        Return string representation of the Rectangle.

        Returns:
            str: String representation of the Rectangle.
        """

        return f"[Rectangle] ({self.id})\
            {self.__x}/{self.__y} -\
            {self.__width}/{self.__height}"
