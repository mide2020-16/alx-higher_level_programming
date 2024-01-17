#!/usr/bin/python3
def uppercase(str):
    i = 0
    n = len(str)
    for c in str:
        i += 1
        if 97 <= ord(c) <= 122:
            print("{}".format(chr(ord(c) - 32)), e='' if i < s else "\n" * (n == 0))
        else:
            print("{}".format(char), e='' if i < s else "\n" * (n == 0))
