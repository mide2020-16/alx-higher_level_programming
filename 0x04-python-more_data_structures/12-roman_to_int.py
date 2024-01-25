#!/usr/bin/python3
def roman_to_int(roman_string):

	# Checks if roman_string is a string and returns None if not
	if not isinstance(roman_string, str) or roman_string is None:
		return None

	# Creates the standard numerals and assign it their value
	roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
									 'C': 100, 'D': 500, 'M': 1000}

	# Set result and the evaluator to 0 initially
	result = 0
	prev_value = 0

	# Iterate through a reversed type of the roman_string
	# so we can do addition and subtraction from the largest number
	for numeral in reversed(roman_string):

		# Gets the value at that particular numeral but here
		# we set 0 just to initialize numeral to 0
		value = roman_numerals.get(numeral, 0)

	# Checks if the value is less than prev_value
	# and do a subtraction else do addition
		if value < prev_value:
			result -= value
		else:
			result += value

	# Sets prev_value to the value after each loop
		prev_value = value

	return result
