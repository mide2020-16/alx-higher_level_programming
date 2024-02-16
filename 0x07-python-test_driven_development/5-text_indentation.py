#!/usr/bin/python3
"""
Function to print text with 2 new lines after '.', '?' and ':'
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':'

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, "{}\n\n".format(char))
    
    print(text, end="")
