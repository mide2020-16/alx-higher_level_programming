#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    argc -= 1
    arg_1 = "argument"
    arg_2 = "arguments"
    if argc == 0:
        print("{} arguments.".format(argc))
    else:
        print("{} {}:".format(argc, arg_1 if argc == 1 else arg_2))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
