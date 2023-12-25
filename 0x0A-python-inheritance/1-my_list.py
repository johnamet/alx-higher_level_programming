#!/usr/bin/python3
"""The module contains MyList class that inherits from
    the list object
"""


class MyList(list):
    """MyList class inherits from the list object
        Args:
        Returns:
    """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """Print sorted prints a sorted list"""

        if any(not isinstance(item, int) for item in self):
            raise TypeError("element needs to be an int")

        print(sorted(self))
