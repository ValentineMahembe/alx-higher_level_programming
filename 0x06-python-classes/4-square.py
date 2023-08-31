#!/usr/bin/python3
""" This module defines a square with a private instance attribute size,
    a property size to retrieve and set its value, and a public instance method area."""


class Square:
    """This class defines a square with a private instance attribute size."""

    def __init__(self, size=0):
        """Initialize a new Square object with the given size.

        Args:
            size (int): The size of the new square. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: Of the size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises: 
            TypeError: If the value is not an integer.
            ValueError: IF the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current square area.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2
