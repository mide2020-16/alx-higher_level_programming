#!/usr/bin/python3
"""checks if a class of an istance is a subclass of another class"""


def inherits_from(obj, a_class):
    """A function that checks if the class of an object
    is a subclass of another class

    Args:
        obj(object): whose class is to be inspected
        a_class(class): the class to be inspected

    Return: True if the class of the object is a subclass of the specified
            class else false is returned
    """
    return issubclass(type(obj), a_class)
