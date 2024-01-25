#!/bin/usr/python3
def uniq_add(my_list=[]):
	new_list = []

	# Iterate through the list and check value is in new_list
	for value in my_list:
		if value not in new_list:
			new_list.append(value)

	# Sum up everything in the new list
	result_sum = sum(new_list)

	return result_sum