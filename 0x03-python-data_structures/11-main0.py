#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

list = [1, 2, 3, 4, 5] 
idx = 3
new_list = delete_at(list, idx)
print(new_list)
print(list)
