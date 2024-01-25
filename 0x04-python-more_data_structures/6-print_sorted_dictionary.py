#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sorted the list using sort()
    sorted_set = sorted(a_dictionary)
    # Iterate through the list and use the key to get it's value
    for key in sorted_set:
        print("{}: {}".format(key, a_dictionary.get(key)))
