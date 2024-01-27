#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    argc = len(names)
    for i in range(argc):
        if "__" in names[i]:
            continue
        print(names[i])
