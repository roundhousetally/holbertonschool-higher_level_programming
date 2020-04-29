#!/usr/bin/python3
rang = range(65, 91)
revarr = reversed(rang)

for alpha in revarr:
    if alpha % 2 == 0:
        alpha = alpha + 32
    print("{}".format(chr(alpha)), end='')
