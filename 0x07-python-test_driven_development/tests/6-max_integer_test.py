#!/usr/bin/python3
""" Unittests for max_integer([..])."""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test max int """
    def test_use(self):
        """ basic use of list of ints """
        self.assertEqual(max_integer([2, 6, 7, 34]), 34)
        self.assertEqual(max_integer([12, 7, 5, 4]), 12)
        self.assertEqual(max_integer([5, 34, 5, 8]), 34)

    def test_flt(self):
        """ test floats """
        self.assertEqual(max_integer([1.3, 5.6, 8.9]), 8.9)
        self.assertEqual(max_integer([8.9, 4.3, 1.4]), 8.9)
        self.assertEqual(max_integer([-4.3, -2, -3]), -2)
        self.assertEqual(max_integer([4.5, 5, 8.4]), 8.4)

    def test_empty(self):
        """ if list empty or None """
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer([None]))

    def test_noarg(self):
        """ no arg """
        self.assertIsNone(max_integer())

    def test_manyargs(self):
        with self.assertRaises(TypeError):
            max_integer([4.5, 5, 8], [9, 10, 50])

    def test_wrongtype(self):
        """ wrong type """
        with self.assertRaises(TypeError):
            max_integer([5, 7, 'T'])
