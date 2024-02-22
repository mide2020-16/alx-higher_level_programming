#!/usr/bin/python3

"""A class called LIst"""


class MyList(list):
    """Prints a list in asccending form"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
