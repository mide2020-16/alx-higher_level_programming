#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    result = 0
    argc = len(argv)
    if argc == 0:
        print("{}".format(0))
    else:
        for i in range(1, len(argv)):
            result += int(argv[i])
        print("{}".format(result))
