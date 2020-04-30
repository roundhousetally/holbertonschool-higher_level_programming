#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 1
    lens = len(argv)
    for i in range(lens):
        if (lens == 1):
            print("{:d} arguments.".format(lens - 1))
            break
        elif (lens == 2):
            print("{:d} argument: ".format(lens - 1))
            break
        elif (lens > 2):
            print("{:d} arguments: ".format(lens - 1))
            break
    for i in range(lens - 1):
        print("{}: {}".format(i + 1, argv[i + 1]))
