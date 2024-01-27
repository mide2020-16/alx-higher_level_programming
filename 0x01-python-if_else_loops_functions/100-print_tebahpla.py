#!/usr/bin/python3
result = "".join(
        chr(i + 32) if i % 2 == 0 else chr(i)
        for i, z in zip(reversed(
                range(ord("A"), ord("Z") + 1)),
                range(27))
        )
print("{}".format(result), end='')
