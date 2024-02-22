#!/usr/bin/python3
"""
a script that adds all arguments to a Python list, and then save them to a file
"""
import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

with open("add_item.json", 'r+') as f:
    save_to_json_file(argv[1:], "add_item.json")
