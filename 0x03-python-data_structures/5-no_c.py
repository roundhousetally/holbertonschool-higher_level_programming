#!/usr/bin/python3
def no_c(my_string):
    mistring = ""
    if (my_string):
        for i in my_string:
            mistring = my_string.translate({ord(i): None for i in 'cC'})
        return (mistring)
