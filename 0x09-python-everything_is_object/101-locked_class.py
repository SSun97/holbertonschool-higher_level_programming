#!/usr/bin/python3
""" A module"""


class LockedClass():
    """A locked class"""

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        self.first_name = first_name
