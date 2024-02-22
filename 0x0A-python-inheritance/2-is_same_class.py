#!/usr/bin/python3
"""checks if an object belongs to a class"""


def is_same_class(obj, a_class):
    """
    Checks for same class

    Args:
        obj (object): An object
        a_class (class): A class

    Return (Bool): True of False
    """
    return type(obj) is a_class
