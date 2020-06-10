#!/usr/bin/python3
""" Unit tests for Base class """


import unittest
import json
import sys
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """ test cases for Base class """
    def test_id(self):
        """ test ids """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(5)
        self.assertEqual(b2.id, 5)

        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json(self):
        """ tests to json method """
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_from_json(self):
        """ tests from json method """

    def test_save_to_file(self):
        """ tests save to file """


class TestBaseFormat(unittest.TestCase):
    """ test the pep8 format """
    def test_pep8(self):
        """ test that its pep8 ok """
        pstyle = pep8.StyleGuide(quiet=True)
        res = pstyle.check_files(['models/base.py', 'models/rectangle.py',
                                     'models/square.py'])
        self.assertEqual(res.total_errors, 0, "Found code style errors (and warnings).")

if __name__ == "__main__":
    unittest.main()
