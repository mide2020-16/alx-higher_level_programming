#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
	# Used list comprehension here
	od_set = {x for x in set_1 | set_2 if x not in set_1 & set_2}
	return od_set