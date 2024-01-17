#!/usr/bin/python3
def uppercase(s):
    i = 0
    n = len(s)
    if s == "":
        return
    for c in s:
        i += 1
        if 97 <= ord(c) <= 122:
            print("{}".format(chr(ord(c) - 32)), end="" if i < n else "\n")
        else:
            print("{}".format(c), end="" if i < n else "\n")
