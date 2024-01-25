#!/bin/usr/python3
def multiply_by_2(a_dictionary):
  # Created a new dictionary
  new_dict = {}
  # Iterate through the key and value
  for key, value in a_dictionary.items():
    # Multiplied the value by 2
    new_dict[key] = value * 2
    # return new dictionary
  return new_dict