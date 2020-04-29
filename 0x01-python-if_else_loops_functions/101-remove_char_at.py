#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    str1 = ''
    for i in range(len(str)):
        if i == n:
            continue
        else:
            str1 = str1 + str[i]
    return str1
