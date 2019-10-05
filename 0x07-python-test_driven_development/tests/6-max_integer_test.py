#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Test Class """
    def test_otraCosa(self):
        """ Test normal values, integers. Picks always the  greater """
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)

    def test_negativeNum(self):
        """ Test normal values, integers. Picks always the  greater """
        self.assertAlmostEqual(max_integer([-1, -2, -1]), -1)

    def test_values(self):
        """ Raise a typeerror if a parameter is None """
        self.assertRaises(TypeError, max_integer, None)

    def test_string(self):
        """ Test a a string inside the list"""
        self.assertRaises(TypeError, max_integer, [1, 2, 'Hello'])

    def test_onlyOneNumber(self):
        """ Test a list with just one number"""
        self.assertAlmostEqual(max_integer([1]), 1)

    def test_emptyList(self):
        """ Takes an empty list """
        self.assertAlmostEqual(max_integer([]), None)

    def test_floatList(self):
        """ Takes a list full of floats """
        self.assertAlmostEqual(max_integer([1.2222, 3.44444, 4.55555]), 4.55555)

    def test_positions(self):
        """ a combination of bigger numbes, at the bg, mid or end """
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([1, 3, 2]), 3)
        self.assertAlmostEqual(max_integer([3, 2, 1]), 3)

    def test_tuple(self):
        """ GEtting a tuple as argument """
        self.assertAlmostEqual(max_integer((1, 2, 3)), 3)

    def test_str_param(self):
        self.assertAlmostEqual(max_integer("Yehaa"), "h")
