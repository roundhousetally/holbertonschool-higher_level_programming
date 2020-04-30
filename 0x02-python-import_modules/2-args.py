#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    lens = len(sys.argv)
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
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
