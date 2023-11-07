#!/usr/bin/python3
"""This module contains a rebel int MyInt that inherits from
    int class
"""


class MyInt(int):
    """MyInt reverses the equality and inequality of the normal int
    """

    def __eq__(self, other):
        super().__ne__(other)

    def __ne__(self, other):
        super().__eq__(other)
