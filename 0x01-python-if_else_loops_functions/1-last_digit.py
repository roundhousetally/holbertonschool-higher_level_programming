#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numb = (abs(number) % 10) * -1
else:
    numb = number % 10
if numb > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, numb))
elif numb == 0:
    print("Last digit of {} is {} and is 0".format(number, numb))
elif numb < 6 and numb != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format
          (number, numb))
