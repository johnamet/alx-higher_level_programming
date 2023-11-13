import unittest
from models.square import Square


class TestSquareMethods(unittest.TestCase):

    def test_init(self):
        # Test initialization with valid values
        square = Square(2, 3, 4, 5)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)
        self.assertEqual(square.id, 5)

        # Test initialization with invalid values
        with self.assertRaises(ValueError):
            Square(-2, 3, 4, 5)

    def test_area(self):
        # Test area calculation
        square = Square(3, 4, 5, 6)
        self.assertEqual(square.area(), 9)

    def test_display(self):
        # Test display method
        square = Square(2, 3, 4, 5)
        expected_output = "  ##\n  ##\n"
        with self.assertLogs(level='INFO'):
            square.display()
            self.assertEqual(square.display(), expected_output)

    def test_str(self):
        # Test string representation
        square = Square(2, 3, 4, 5)
        self.assertEqual(str(square), "[Square] (5) 3/4 - 2")

    def test_update(self):
        # Test update method
        square = Square(2, 3, 4, 5)
        square.update(10, 20, 30, 40)
        self.assertEqual(square.__str__(), "[Square] (10) 30/40 - 20")

    def test_to_dictionary(self):
        # Test to_dictionary method
        square = Square(2, 3, 4, 5)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 5, 'size': 2, 'x': 3, 'y': 4}
        self.assertEqual(square_dict, expected_dict)