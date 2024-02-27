#!/usr/bin/python3
"""
A Square shape and class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
        size (int): Size of the square.
        x (int): x-coordinate of the square's position.
        y (int): y-coordinate of the square's position.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): x-coordinate of the square's position. Defaults to 0.
            y (int, optional): y-coordinate of the square's position. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """

        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """
        Convert Square attributes to a dictionary.

        Returns:
            dict: Dictionary containing attributes of the Square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes with both positional and keyword arguments.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.width = value
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def __str__(self):
        """
        Return string representation of the Square.

        Returns:
            str: String representation of the Square.
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
