#!/usr/bin/python3
"""This is a testcase to test the rectangle class"""
from models.rectangle import Rectangle
import unittest


class RectangleTestCase(unittest.TestCase):

    def setUp(self):
        # Create a Rectangle instance with default values
        self.rectangle = Rectangle(2, 3)

    def test_width_attribute(self):
        # Test the width attribute
        self.assertEqual(self.rectangle.width, 2)

        # Set a new width value
        self.rectangle.width = 5
        self.assertEqual(self.rectangle.width, 5)

        # Test if ValueError is raised for non-positive numbers
        with self.assertRaises(ValueError):
            self.rectangle.width = -1

        # Test if TypeError is raised for non-integer width
        with self.assertRaises(TypeError):
            self.rectangle.width = "invalid"
            self.rectangle.width = 1.5

    def test_height_attribute(self):
        # Test the height attribute
        self.assertEqual(self.rectangle.height, 3)
        
        # Set a new height value
        self.rectangle.height = 9
        self.assertEqual(self.rectangle.height, 9)

        # Test if ValueError is raised for non-positive height
        with self.assertRaises(ValueError):
            self.rectangle.height = -1

        # Test if TypeError is raised for non-integer height
        with self.assertRaises(TypeError):
            self.rectangle.height = "invalid"
            self.rectangle.height = 3.5

    def test_x_attribute(self):
        # Test the x attribute
        self.assertEqual(self.rectangle.x, 0)
        
        # Set new x value
        self.rectangle.x = 4
        self.assertEqual(self.rectangle.x, 4)

        # Test if ValueError is raised for non-positive x
        with self.assertRaises(ValueError):
            self.rectangle.x = -1

        # Test if TypeError is raised for non-integer x
        with self.assertRaises(TypeError):
            self.rectangle.x = "invalid"
            self.rectangle.x = 6.5

    def test_y_attribute(self):
        # Test the y attribute
        self.assertEqual(self.rectangle.y, 0)

        # Set new y value
        self.rectangle.y = 4
        self.assertEqual(self.rectangle.y, 4)

        # Test if ValueError is raised for non-positive y
        with self.assertRaises(ValueError):
            self.rectangle.y = -5

        # Test if TypeError is raised for non-integer value
        with self.assertRaises(TypeError):
            self.rectangle.y = "invalid"
            self.rectangle.y = 3.5
