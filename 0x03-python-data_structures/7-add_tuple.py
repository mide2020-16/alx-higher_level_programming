#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    element_a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    element_a2 = tuple_a[1] if len(tuple_a) >= 2 else 0

    element_b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    element_b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    return (element_a1 + element_b1, element_a2 + element_b2)
