#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_digit = number % 10
    else:
        last_digit = number % -10
    print(f"{last_digit}".format())

print_last_digit(-98)
