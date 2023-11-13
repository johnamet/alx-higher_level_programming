#!/usr/bin/python3
from models.square import Square
import unittest


class TestSquareAttributes(unittest.TestCase):
    # Set up the square instance with default value
    def setUp(self):
        self.square = Square(4)

    def test_size(self):
        # Test the size of square
        self.assertEqual(self.square.width, 4)

        # Set new value for the size
        self.square.width = 7
        self.assertEqual(self.square.width, 7)

        # Test if TypeError is raised for non-integer size
        with self.assertRaises(TypeError):
            self.square.width = "invalid"
            self.square.width = 3.5

        # Test if ValueError is raisef for non-positive size
        with self.assertRaises(ValueError):
            self.square.width = -2

    def test_x_attribute(self):
        # Test the x attribute
        self.assertEqual(self.square.x, 0)

        # Test new x attribute
        self.square.x = 4
        self.assertEqual(self.square.x, 4)

        #Test if ValueError is raised for non-positive x
        with self.assertRaises(ValueError):
            self.square.x = -8

        #Test if TypeError is raised for non-integer x
        with self.assertRaises(TypeError):
            self.square.x = "invlaid"
            self.square.x = 3.5

    def test_y_attribute(self):
        # Test the y attribute
        self.assertEqual(self.square.y, 0)

        # Test new y attribute
        self.square.y = 4
        self.assertEqual(self.square.y, 4)

        #Test if ValueError is raised for non-positive y
        with self.assertRaises(ValueError):
            self.square.y = -8

        #Test if TypeError is raised for non-integer y
        with self.assertRaises(TypeError):
            self.square.y = "invlaid"
            self.square.y = 3.5

    def test_area_method(self):
        self.setUp()
        self.assertEqual(self.square.area(), 16)

    def test_update_method(self):
        # Test the args
        # Test update the id
        self.square.update(18)
        self.assertEqual(self.square.id, 18)

        # Test the args id and size
        self.square.update(18, 5)
        self.assertEqual(self.square.size, 5)

        # Test the args id, size and x
        self.square.update(18, 5, 6)
        self.assertEqual(self.square.x, 6)

        # Test the args id, size, x, y
        self.square.update(18, 5, 4, 6)
        self.assertEqual(self.square.y, 6)

        # Test the kwargs with id
        self.square.update(id=2)
        self.assertEqual(self.square.id, 2)

        # Test the kwargs with size
        self.square.update(size=15)
        self.assertEqual(self.square.size, 15)

        # Test the kwargs with x
        self.square.update(x=4)
        self.assertEqual(self.square.x, 4)

        # Test the kwargs with y
        self.square.update(y=5)
        self.assertEqual(self.square.y, 5)
