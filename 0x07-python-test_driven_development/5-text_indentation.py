#!/usr/bin/python3
"""  Text Indendation Mod """


def text_indentation(text):
    """ prints a text with 2 new lines
    after each of the chars: . ? :
    Args: text """
    d = ['.', '?', ':']
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in d:
        text = text.replace(i, i + '\n\n')
    final = [line.strip() for line in text.split('\n')]
    final = '\n'.join(final)
    print(final, end='')
