#!/usr/bin/python3
""" student mod """


class Student:
    """
    Student class, full name and age
    """
    def __init__(self, first_name, last_name, age):
        """ instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dict rep """
        if type(attrs):
            return self.__dict__
        else:
            return self.__dict__
