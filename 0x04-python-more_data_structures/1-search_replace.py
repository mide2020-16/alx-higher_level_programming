#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Use list comprehension to create a new list with replaced values
    new_list = [replace if item == search else item for item in my_list]
    return new_list