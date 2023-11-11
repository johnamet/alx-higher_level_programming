#!/usr/bin/python3
"""This is a test suite to test the Base class"""
from models.base import Base
import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.base = Base()

    def test_id_none(self):
        self.assertEqual(self.base.id, 1)

    def test_id_not_none(self):
        self.base.id = 4
        self.assertEqual(self.base.id, 4)
