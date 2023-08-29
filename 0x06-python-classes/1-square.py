#!/usr/bin/python3
"""Working with Python doing Object Oriented Prog."""


class Square:
    """This class deffines a square with a private instance attribute size."""

    def __init__(self, size):
        """Initiaze a new Square object with a given size.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
