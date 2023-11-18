from turtle import Turtle, colormode, done
import math

def draw_rectangle(turtle_obj: Turtle, x: float, y: float, width: int, height: int):
    """ Function to draw a rectangle"""
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    half: int = 0
    while half < 2:
        turtle_obj.forward(width)
        turtle_obj.right(90)
        turtle_obj.forward(height)
        turtle_obj.right(90)
        half += 1
    turtle_obj.end_fill()

def draw_circle(turtle_obj: Turtle, x: float, y: float, radius: float):
    """ Function to draw a circle """
    turtle_obj.penup()
    turtle_obj.goto(x, y - radius)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    circumference = 2 * math.pi * radius
    side_length = circumference / 360
    angle = 1
    while angle <= 360:
        turtle_obj.forward(side_length)
        turtle_obj.right(1)
        angle += 1
    turtle_obj.end_fill()

def draw_triangle(turtle_obj: Turtle, x: float, y: float, size: float):
    """Function to draw a triangle"""
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    count_sides: int = 0
    while count_sides <= 2:
        turtle_obj.forward(size)
        turtle_obj.left(120)
        count_sides += 1
    turtle_obj.end_fill()

def main():
    """Main function"""
    colormode(255)  # Set color mode to 255
    leo = Turtle()
    leo.speed(0)

    # Draw trunk using rectangles
    leo.color("brown")
    draw_rectangle(leo, -25, -100, 50, 100)
    
    # Draw canopy using circles and triangles
    leo.color("green")
    draw_circle(leo, 0, 0, 50)
    draw_triangle(leo, 0, 50, 60)

    done()

if __name__ == "__main__":
    main()