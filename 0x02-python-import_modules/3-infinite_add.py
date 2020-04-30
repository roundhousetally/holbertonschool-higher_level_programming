#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 0
    sum1 = 0
    lens = len(argv)
    for i in range(lens):
        sum1 += int(i)
    print("{}".format(sum1))
