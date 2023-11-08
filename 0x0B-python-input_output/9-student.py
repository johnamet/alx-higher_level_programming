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

    def to_json(self):
        student_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        return student_dict
