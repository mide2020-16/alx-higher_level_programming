#!/usr/bin/python3
"""
A function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): The filename

    Return: void
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        read_data = f.read()
        print(read_data, end="")
