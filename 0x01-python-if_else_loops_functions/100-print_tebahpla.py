#!/usr/bin/python3


for i, j in zip(range(90, 65, -2), range(122, 97, -2)):
    print(f"{chr(j)}{chr(i-1)}", end='')
