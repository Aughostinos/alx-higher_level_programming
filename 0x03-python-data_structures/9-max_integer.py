#!/usr/bin/python3
def max_integer(my_list=[]):
    lenlist = len(my_list)
    if lenlist == 0:
        return None
    else:
        my_list.sort()
        return my_list[lenlist-1]
