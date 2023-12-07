#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    my_list = []
    for key, value in a_dictionary.items():
        my_list.append(value)
    return max(my_list)
