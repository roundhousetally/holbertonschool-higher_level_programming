#!/usr/bin/python3
""" inheritence mod """


class MyList(list):
    """ child class """
    def print_sorted(self):
        """ print """
        if issubclass(MyList, list):
            print(sorted(self))
