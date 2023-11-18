"""Importing the module to check the correctness."""
from point import Point

x = 1.0
y = 2.0
Point_example = Point(x, y)
print(Point_example.x, Point_example.y)
Point_example.scale_by(2)
print(Point_example.x, Point_example.y)
Point_example2 = Point_example.scale(2)
print(Point_example2.x, Point_example2.y)