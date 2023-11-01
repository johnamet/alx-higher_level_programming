#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    def test_values(self):
        #Test if the list empty
        self.assertRaises(ValueError, max_integer, [])

        #Test if the function takes lists containing only integers
        self.assertRaises(ValueError, max_integer, ["1", 3, True, 4.0])

    def test_types(self):
        #Test if the function accepts only lists
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, "mom")
        self.assertRaises(TypeError, max_integer, 4)
    """

    def test_max_integer(self):
        # Test max integer when list is not empty
        self.assertEqual(max_integer([1, 3, 4, 52, 4]), 52)
        self.assertEqual(max_integer([-1, 0, -2, -4]), 0)
        self.assertEqual(max_integer([5, 4, 2, 1]), 5)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([]), None)
