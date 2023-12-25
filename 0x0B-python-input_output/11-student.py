#!/usr/bin/python3
"""The student class mdule"""


class Student:
    """The student class defines a student by first name,
        last_name and age.
    Attributes:
        first_name (str): the first name of the student
        last_name (str): last name of the student
        age (int): the age of the student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs):
        student_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        if isinstance(attrs, list) and all(isinstance(item, str)
                                           for item in attrs):
            new_dict = {}
            # loop through the list of attribute names
            for attr in attrs:
                # check if the attribute exists in the student object
                if hasattr(self, attr):
                    # add the attribute and its value to the new dictionary
                    new_dict[attr] = getattr(self, attr)
            # return the new dictionary
            return new_dict
        else:
            # return the original dictionary
            return student_dict

    def reload_from_json(self, json):
        """A method that replaces the student's
            attributes with the values from a json dictionary
        """

        for key, value in json.items():
            # Update the attribute with the corresponding value
            setattr(self, key, value)
