#!/usr/bin/python3
""" function that returns a tuple with the length of the string and its first char """


def multiple_returns(sentence):
    i = 0
    strl = len(sentence)
    if strl == 0:
        a = 0
        b = None
        tuple_sent = a, b

    else:
        tuple_sent = (strl, sentence[i])
    return (tuple_sent)
