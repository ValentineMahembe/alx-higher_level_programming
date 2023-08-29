#!/usr/bin/python3
"""A class square that defines a square."""


class Square:
    """This class defines a square with a private instance attribute size."""

    def __init__(self, size=0):
        """Initialize a new Square object with the given size.

        Args:
            size (int): The size of the new square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: Is size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
