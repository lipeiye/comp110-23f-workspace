"""CQ07 class practise."""
from __future__ import annotations

__author__ = "730698337"


class Point:
    """The class method."""

    def __init__(self, x_init: float, y_init: float) -> None:
        """The init method."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """A method scale the object."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """A method create a new object which is already scaled."""
        new_x = self.x * factor
        new_y = self.y * factor
        return Point(new_x, new_y)
    