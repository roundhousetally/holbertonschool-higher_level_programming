#!/usr/bin/python3
import inspect
from inspect import getmembers
import hidden_4
if __name__ == "__main__":
    i = 0
    for name, data in inspect.getmembers(hidden_4):
        if name[i] == '_':
            continue
        print("{}".format(name))
