#!/usr/bin/python3
def no_c(my_string):
    mistring = ""
    if (my_string):
        for i in my_string:
            if (i != 'c' and i != 'C'):
                mistring = mistring + i
        return (mistring)
