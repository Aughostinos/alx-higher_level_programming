#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter = 0

    for element in range(x):
        try:
            print(my_list[element], end="")
        except IndexError:
            print("index error")
    return counter
