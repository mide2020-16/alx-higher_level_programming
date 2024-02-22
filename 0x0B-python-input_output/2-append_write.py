#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
	"""
	Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added

	Args:
		filename (str): Filename
		text (str): text

	Return: len of text
	"""
	with open(filename, 'a', encoding="UTF-8") as File:
		return File.write(text)
