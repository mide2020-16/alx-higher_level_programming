#!/usr/bin/python3
def best_score(a_dictionary):
	# Check if dictionary is empty and return None
	if a_dictionary is None:
		return None

	# Assigned key initially none and the max_value
	# smallest possible number
	best_key = None
	max_value = float('-inf')

	for key, value in a_dictionary:
		if value > max_value:
			max_value = value
			best_key = key

	return best_key