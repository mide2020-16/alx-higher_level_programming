#!/usr/bin/python3
def uppercase(s):
    i = 0
    n = len(s)

    for char in s:
        i += 1
        if 97 <= ord(char) <= 122:
            print("{}".format(chr(ord(char) - 32)), end="" if i < n else "\n" * (n == 0))
        else:
			print("{}".format(char), end="" if i < n else "\n" * (n == 0))
			
