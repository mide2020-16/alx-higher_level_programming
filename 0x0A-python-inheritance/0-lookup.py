#!/usr/bin/python3
"""
Function that lookup an object attribute
"""


def lookup(obj):
    """
    Look up an object

    Args:
        obj (object): The object

    Return:
        Bool: either true or false
    """
    return [attr for attr in dir(obj)]
