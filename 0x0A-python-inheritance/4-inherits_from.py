#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Inherits from a base class"""

    return issubclass(type(obj), a_class)
