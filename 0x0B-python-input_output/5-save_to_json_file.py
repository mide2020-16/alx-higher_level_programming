#!/usr/bin/python3
"""Writes object to a file"""
import json


def save_to_json_file(my_obj, filename):
	"""Writes object to a file"""

	with open(filename, 'w') as f:
		return f.write(json.dumps(my_obj))
