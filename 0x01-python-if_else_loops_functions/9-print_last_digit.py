#!/usr/bin/python3
def print_last_digit(number):
    numb = 0
    if number < 0:
        number = abs(number)
    numb = number % 10
    print("{}".format(numb), end='')
    return numb
