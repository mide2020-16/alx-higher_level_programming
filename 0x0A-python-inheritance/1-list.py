#!/usr/bin/python3
"""A class called List"""


class MyList(list):
    """
    A list implementation

    Args:
        list (list): A list of int

    Return: the sorted list
    """

    def print_sorted(self):
        """Prints list in ascending order"""

        sorted_list = sorted(self)
        print(sorted_list)
