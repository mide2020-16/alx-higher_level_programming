#!/usr/bin/python3
"""
Pascal Triangle for n value
"""


# def pascal_triangle(n):

#     if n <= 0:
#         return []

#     pascal = []

#   def combination(n):

#   def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

#     result = []
#     for i in range(n + 1):
#         result.append(factorial(n) // (factorial(n - i) * factorial(i)))
#     return result

#     if not isinstance(n, int):
#         return f"{n} is not an integer"
#     for i in range(n):
#         pascal.append(combination(i))
#     return pascal


def pascal_triangle(n):
    """
    Pascal Triangle formation

    Args:
        n (int): value

    Return: dict
    """
    if n <= 0:
        return []

    pascal = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        pascal.append(row)
    return pascal
