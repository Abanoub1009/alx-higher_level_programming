#!/usr/bin/python3
def element_at(my_list, idx):
    n = len(my_list)
    if 0 <= idx < n:
        return my_list[idx]
    return None
