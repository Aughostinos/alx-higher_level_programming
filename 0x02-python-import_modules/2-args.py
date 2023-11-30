#!/usr/bin/python3
import sys
def print_argument(argv):
    arg_number = len(argv)

    if arg_number == 0:
        print("0 argument.")
    elif arg_number == 1:
        print(f"1 argument:\n1: {argv[0]}".format())
    else:
        print(f"{arg_number} arguments:")
        for i in argv:
            print(f"{i}: {argv[1]}".format())

    if __name__ == "__main__":
        arguments = sys.argv[1:]
        print_argument(arguments)
