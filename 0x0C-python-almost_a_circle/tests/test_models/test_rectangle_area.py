import unittest
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):

    def setUp(self):
        # Create a Rectangle instance with default values
        self.rectangle = Rectangle(2, 3)

    def test_area_property_with_default_values(self):
        self.assertEqual(self.rectangle.area, 6)

    def test_area_property(self):
        # Test with new values of width and height
        self.rectangle.height = 4
        self.rectangle.width = 2

        # Ensure that the area property returns the correct value
        self.assertEqual(self.rectangle.area, 8)
