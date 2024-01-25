#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	# Created an empty list
	new_matrix = []

	# Loop through each row and used lambda to map and
	# also append the result to created list
	for row in matrix:
		squared_row = list(map(lambda x: x ** 2, row[:]))
		new_matrix.append(squared_row)

	return new_matrix
