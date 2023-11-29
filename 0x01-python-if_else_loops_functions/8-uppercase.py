#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for c in str:
        if 'a' <= c <= 'z':
            uppercase_str += chr(ord(c) - 32)
        else:
            uppercase_str += chr
            
    print(f"{uppercase_str}".format())
