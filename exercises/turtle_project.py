"""EX05_turtle_scene."""
__author__ = "730698337"
from turtle import Turtle, colormode, done


def draw_rectangle(turtle_obj: Turtle, x: float, y: float, width: int, height: int) -> None:
    """Function to draw a rectangle."""
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    half: int = 0
    while (half < 2):
        turtle_obj.forward(width)
        turtle_obj.right(90)
        turtle_obj.forward(height)
        turtle_obj.right(90)
        half += 1
    turtle_obj.end_fill()


def draw_circle(turtle_obj: Turtle, x: float, y: float, radius: float) -> None:
    """Function to draw a circle."""
    turtle_obj.penup()
    turtle_obj.goto(x, y - radius)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    turtle_obj.circle(radius)
    turtle_obj.end_fill()


def draw_triangle(turtle_obj: Turtle, x: float, y: float, size: float) -> None:
    """Function to draw a triangle."""
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    count_sides: int = 0
    while (count_sides <= 3):
        turtle_obj.forward(size)
        turtle_obj.left(120)
        count_sides += 1
    turtle_obj.end_fill()


def draw_pentagon(turtle_obj: Turtle, x: float, y: float, size: float) -> None:
    """Function to draw a pentagon (five-sided star)."""
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    angle: int = 144
    count_sides: int = 0
    while (count_sides < 5):
        turtle_obj.forward(size)
        turtle_obj.right(angle)
        count_sides += 1
    turtle_obj.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    colormode(255)
    leo: Turtle = Turtle()
    draw_rectangle(leo, -70.0, -110.0, 60, 200)
    leo.color("green")
    draw_triangle(leo, -170.0, -110.0, 260)
    draw_triangle(leo, 50, 115.166, 200)
    leo.color("red")
    draw_circle(leo, -63.0, 65.0, 10.3)
    draw_circle(leo, -125.0, -60, 10.3)
    draw_circle(leo, -12.0, -15.0, 10.3)
    draw_circle(leo, -10.3, 160.2, 10.3)
    draw_circle(leo, -82.3, 174.2, 10.3)
    leo.color("yellow")
    draw_pentagon(leo, 180, 300, 100)
    draw_pentagon(leo, 285, 285, 60)
    done()


if __name__ == "__main__":
    main()