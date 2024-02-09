#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    try:
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    printed_count += 1
            except ValueError:
                pass
    except IndexError:
        pass
    finally:
        print()
        return printed_count
