#!/usr/bin/python3
"""This is a test suite to test the Base class"""
from models.base import Base
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.base = Base()
    
    
    def test_id_attribute(self):
        # Test id attribute
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)

        # Test id attribute with custom id
        base_instance_custom_id = Base(10)
        self.assertEqual(base_instance_custom_id.id, 10)

        # Test id attribute with consecutive instances
        base_instance_consecutive = Base()
        self.assertEqual(base_instance_consecutive.id, 2)

    def test_id_none(self):
        self.assertEqual(self.base.id, 1)

    def test_id_not_none(self):
        self.base.id = 4
        self.assertEqual(self.base.id, 4)

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

    def test_save_to_file(self):
        # Test saving an empty list to a file
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

        # Test saving a list with instances to a file
        rect = Rectangle(1, 2)
        square = Square(3)
        instances = [rect, square]
        Base.save_to_file(instances)
        with open("Base.json", "r") as file:
            content = file.read()
            expected_output = '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}, {"id": 2, "size": 3, "x": 0, "y": 0}]'
            self.assertEqual(content, expected_output)

    def test_load_from_file(self):
        # Test loading from a non-existing file
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

        # Test loading from an existing file
        rect = Rectangle(1, 2)
        square = Square(3)
        instances_to_save = [rect, square]
        Base.save_to_file(instances_to_save)
        loaded_instances = Base.load_from_file()
        self.assertEqual(len(loaded_instances), 2)
        self.assertEqual(loaded_instances[0].__str__(), rect.__str__())
        self.assertEqual(loaded_instances[1].__str__(), square.__str__())

    def test_save_to_file_csv(self):
        # Test saving an empty list to a CSV file
        Base.save_to_file_csv([])
        with open("Base.csv", "r") as file:
            content = file.read()
            self.assertEqual(content, "")

        # Test saving a list with instances to a CSV file
        rect = Rectangle(1, 2)
        square = Square(3)
        instances = [rect, square]
        Base.save_to_file_csv(instances)
        with open("Base.csv", "r") as file:
            content = file.read()
            expected_output = "id,width,height,x,y\n1,1,2,0,0\n2,3,3,0,0\n"
            self.assertEqual(content, expected_output)

    def test_load_from_file_csv(self):
        # Test loading from a non-existing CSV file
        instances = Base.load_from_file_csv()
        self.assertEqual(instances, [])

        # Test loading from an existing CSV file
        rect = Rectangle(1, 2)
        square = Square(3)
        instances_to_save = [rect, square]
        Base.save_to_file_csv(instances_to_save)
        loaded_instances = Base.load_from_file_csv()
        self.assertEqual(len(loaded_instances), 2)
        self.assertEqual(loaded_instances[0].__str__(), rect.__str__())
        self.assertEqual(loaded_instances[1].__str__(), square.__str__())

    def test_draw(self):
        # Test drawing rectangles and squares
        rect = Rectangle(1, 2)
        square = Square(3)
        instances = [rect, square]
        Base.draw(rect, square)

