#!/usr/bin/python3

def lookup(obj):
    """Checks for the attribute and methods of "obj" """

    return [attr for attr in dir(obj)]
