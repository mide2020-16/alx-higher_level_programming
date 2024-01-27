#!/usr/bin/python3
# Using list comprehension
# print(''.join([chr(i + 32) if i % 2 == 0 
# else chr(i) for i, z in zip(reversed(range(ord('A'),
# ord('Z') + 1)), range(27))]))

value = []
max_value = 32

for i, z in zip(reversed(range(ord('A'), ord('Z') + 1)), range(27)):
    if i % 2 == 0:
        value.append(chr(i + max_value))
    elif i % 2 != 0:
        value.append(chr(i))
print(''.join(''.join(value)), end='')
