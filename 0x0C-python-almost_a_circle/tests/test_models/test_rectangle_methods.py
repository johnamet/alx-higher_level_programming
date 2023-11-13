import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):

    def test_init(self):
        # Test initialization with valid values
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 5)

        # Test initialization with invalid values
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 4, 5)

    def test_area(self):
        # Test area calculation
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_display(self):
        # Test display method
        rect = Rectangle(2, 3)
        expected_output = "  ##\n  ##\n  ##\n"
        with self.assertLogs(level='INFO'):
            rect.display()
            self.assertEqual(rect.display(), expected_output)

    def test_str(self):
        # Test string representation
        rect = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 4/5 - 2/3")

    def test_update(self):
        # Test update method
        rect = Rectangle(2, 3, 4, 5, 1)
        rect.update(10, 20, 30, 40, 50)
        self.assertEqual(rect.__str__(), "[Rectangle] (10) 30/40 - 20/50")

    def test_to_dictionary(self):
        # Test to_dictionary method
        rect = Rectangle(2, 3, 4, 5, 1)
        rect_dict = rect.to_dictionary()
        expected_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        self.assertEqual(rect_dict, expected_dict)

