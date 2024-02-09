#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0
            if not isinstance(elem_1, (int, float)) or not isinstance(
                elem_2, (int, float)
            ):
                print("wrong type")
                result.append(0)
                continue
            if elem_2 == 0:
                raise ZeroDivisionError
            result.append(elem_1 / elem_2)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
