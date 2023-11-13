import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBaseMethods(unittest.TestCase):

    def test_to_json_string(self):
        # Test when list is empty
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test when list is not empty
        rect = Rectangle(1, 2)
        square = Square(3)
        instances = [rect, square]
        expected_output = '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}, {"id": 2, "size": 3, "x": 0, "y": 0}]'
        self.assertEqual(Base.to_json_string(instances), expected_output)

    def test_from_json_string(self):
        # Test when the string is empty
        self.assertEqual(Base.from_json_string(""), [])

        # Test when the string is not empty
        input_str = '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}, {"id": 2, "size": 3, "x": 0, "y": 0}]'
        expected_output = [
            {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0},
            {"id": 2, "size": 3, "x": 0, "y": 0}
        ]
        self.assertEqual(Base.from_json_string(input_str), expected_output)

    def test_create(self):
        # Test creating a Rectangle instance
        rect_instance = Rectangle(1, 2, 3, 4, 5)
        rect_dict = rect_instance.to_dictionary()
        created_rect = Base.create(**rect_dict)
        self.assertEqual(created_rect.__str__(), rect_instance.__str__())

        # Test creating a Square instance
        square_instance = Square(3, 2, 1, 5)
        square_dict = square_instance.to_dictionary()
        created_square = Base.create(**square_dict)
        self.assertEqual(created_square.__str__(), square_instance.__str__())
