#!/usr/bin/python3
""" unit tests for Rectangle class """


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ test cases for Rectangle class """
    def test_argless(self):
        """ test no args """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_width(self):
        """ test height """
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4).__width)

    def test_height(self):
        """ test width """
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4).__height)

    def test_area(self):
        """ test area """

    def test_str(self):
        """ test str """

    def test_dictionary(self):
        """ test dict """

    def test_update(self):
        """ update test """

    def test_x(self):
        """ test x """

    def test_y(self):
        """ test y """

    if __name__ == '__main__':
        unittest.main()
