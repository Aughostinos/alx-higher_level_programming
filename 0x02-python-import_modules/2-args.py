#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_number = len(sys.argv)

    if arg_number - 1 == 0:
        print("0 argument.")
    elif arg_number - 1 == 1:
        print(f"1 argument:".format())
        print(f"1: {sys.argv[1]}".format())
    else:
        print(f"{arg_number - 1} arguments:".format())
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}".format())
