#!/usr/bin/python3
"""This is a base model class"""
import json
import csv
import turtle


class Base:
    """This is a base class
    Attributes:
        nb_objects (int):m Number of objects

    Args:
        id (int): an id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """The method returns json representation of
            list dictionaries
        Args:
            list_dictionaries (obj): is a list of dictionaries
        """
        if not list_dictionaries and len(list_dictionaries) == 0:
            return "[]"
        else:
            json_str = json.dumps(list_dictionaries)

        return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json representation of list_objs to a file
        Args:
            cls (obj): Class object to represent
            list_objs (obj): List of objects
        """
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)

        list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(filename, encoding="UTF8", mode="w") as f:
            f.write(Base.to_json_string(list_dicts))

    def from_json_string(json_string):
        """The method parses a list of dict into json
            string
        Args:
            json_string (str): string representation of json_string
        """

        if not json_string or len(json_string) == 0:
            return []
        else:
            obj = json.loads(json_string)

        return obj

    @classmethod
    def create(cls, **dictionary):
        """The method creates an already-made instances of a class
        Args:
            cls (cls): the class object to create
            dictionary (obj): The passed arguments
        Return:
            :obj: the dummy object
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(2, 3)
        elif cls.__name__ == "Square":
            dummy_instance = cls(2)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)
        return dummy_instance

    def update(self, *args, **kwargs):
        """The update method updates the cls attributes"""

        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def load_from_file(cls):
        """load_from_file loads the class attributes from a json
            file based on the object class
        """

        filename = "{}.json".format(cls.__name__)
        instances = []
        try:
            with open(filename, encoding="UTF8", mode="r") as f:
                read_data = f.read()
                loaded_inst = cls.from_json_string(read_data)
                for dic in loaded_inst:
                    instances.append(cls.create(**dic))
        except FileNotFoundError:
            instances = []

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """The method saves to a csv file
        Args:
            list_objs (:obj):  list of objects to save
        """

        if not list_objs:
            list_objs = []

        filename = "{}.csv".format(cls.__name__)

        list_dict = [obj.to_dictionary() for obj in list_objs]
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]

        with open(filename, 'w', newline="", encoding="UTF8") as csv_f:
            writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
            writer.writeheader()

            writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """This loads a class attibutes from a csv file
        """

        filename = "{}.csv".format(cls.__name__)
        instances = []
        loaded_attri = []
        try:
            with open(filename, encoding="UTF8", mode="r") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    row["id"] = int(row["id"])
                    if cls.__name__ == "Rectangle":
                        row["width"] = int(row["width"])
                        row["height"] = int(row["height"])
                    else:
                        row["size"] = int(row["size"])
                    row["x"] = int(row["x"])
                    row["y"] = int(row["y"])
                    loaded_attri.append(dict(row))

                for inst in loaded_attri:
                    instances.append(cls.create(**inst))
        except FileNotFoundError:
            instances = []

        return instances

    def draw(list_rectangles, list_squares):
        """The draw method draws a rectangles or squares
        using turtle class.
        Args:
            list_rectangles (obj): The list of rectangle instances
            list_squares (obj): The list of square instances
        """

        screen = turtle.Screen()
        screen.bgcolor("white")

        for rec in list_rectangles:
            tturtle = turtle.Turtle()
            x = rec.x
            y = rec.y
            width = rec.width
            height = rec.height
            tturtle.position(x, y)

            for _ in range(4):
                tturtle.forward(height)
                tturtle.left(width)

            tturtle.hideturtle()

        for sq in list_squares:
            tturtle = turtle.Turtle()
            x = sq.x
            y = sq.y
            size = sq.size
            tturtle.position(x, y)

            for _ in range(4):
                tturtle.forward(size)
                tturtle.left(size)

            tturtle.hideturtle()

        turtle.mainloop()
