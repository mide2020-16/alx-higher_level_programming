#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
	"""
	Write a function that writes a string to a text file (UTF8) and returns the number of characters written

	Args:
		filename (str): Filename
		text (str): text

	Return: len of text
	"""
	with open(filename, 'w', encoding="UTF-8") as File:
		return File.write(text)
