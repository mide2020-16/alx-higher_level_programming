#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text
"""


def append_write(filename="", text=""):
    """
    Write a function that appends a string at the end of a text

    Args:
        filename (str): Filename
        text (str): text

    Return: len of text
    """
    with open(filename, 'a', encoding="UTF-8") as File:
        return File.write(text)
