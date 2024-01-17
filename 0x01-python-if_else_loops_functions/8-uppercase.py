#!/usr/bin/python3
def uppercase(str):
    i = 0
    n = len(str)
    for char in str:
        i = i + 1
        if 97 <= ord(char) <= 122:
            print("{}".format(chr(ord(char) - 32)), end=" if i < n else "\n")
        else:
            print("{}".format(char), end="" if i < n else "\n")
