#!/usr/bin/python3
"""this script checks if a object is an istance of a class
    or its subclass
"""


def is_kind_of_class(obj, a_class):
    """
    Checks kind of class an obj is

    Args:
        obj (object): An object
        a_class (class): A class

    Return (Bool): True or False
    """
    return isinstance(obj, a_class)
