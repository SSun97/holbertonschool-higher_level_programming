#!/usr/bin/python3
"""
    Write a class MyList that inherits from list:
"""


class MyList(list):
    """Same as moulde """

    def __init__(self):
        """init a function"""

        super().__init__()

    def print_sorted(self):
        """Print sorted list"""

        print(sorted(self))
