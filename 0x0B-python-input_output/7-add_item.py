#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then saves them to a file.
"""
from sys import argv  # Importing argv to access command line arguments


# Importing the save_to_json_file function from 5-save_to_json_file.py
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
# Importing the load_from_json_file function from 6-load_from_json_file.py
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Opening the file 'add_item.json' in read and write mode ('r+')
with open("add_item.json", 'r+') as f:
    # Saving the command line arguments (excluding the script name) to 'add_item.json'
    save_to_json_file(argv[1:], "add_item.json")
    load_from_json_file(argv[1])
