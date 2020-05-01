#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    lens = len(argv)
    if lens == 1:
        print(sum)
    elif lens == 2:
        sum = argv[1]
        print(sum)
    else:
        for i in range(1, lens):
            sum += int(argv[i])
        print("{}".format(sum))
