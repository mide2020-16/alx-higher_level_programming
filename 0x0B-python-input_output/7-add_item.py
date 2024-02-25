#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then saves them to a file.
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_josn_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_json(filename):
    """
    Add items provided as command line arguments to a JSON file.

    Args:
        filename (str): The name of the JSON file to which the items will be added.

    Returns:
        None
    """
    # Open the file in read and write mode ('r+')
    with open(filename, 'r+') as f:
        # Save command line arguments (excluding script name) to the JSON file
        save_to_json_file(argv[1:], filename)
        # Load items from the JSON file (optional, just for demonstration)
        load_from_json_file(filename)
