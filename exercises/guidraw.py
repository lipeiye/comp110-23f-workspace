import turtle

# Function to draw the trunk of the tree
def draw_trunk(turtle_obj, trunk_height, trunk_width):
    turtle_obj.color("brown")
    turtle_obj.begin_fill()
    turtle_obj.forward(trunk_width / 2)
    turtle_obj.right(90)
    turtle_obj.forward(trunk_height)
    turtle_obj.right(90)
    turtle_obj.forward(trunk_width)
    turtle_obj.right(90)
    turtle_obj.forward(trunk_height)
    turtle_obj.right(90)
    turtle_obj.forward(trunk_width / 2)
    turtle_obj.end_fill()

# Function to draw branches of the tree
def draw_branches(turtle_obj, branch_length, levels):
    if levels == 0:
        return
    turtle_obj.color("green")
    turtle_obj.pensize(levels)
    turtle_obj.forward(branch_length)
    turtle_obj.right(30)
    draw_branches(turtle_obj, branch_length * 0.7, levels - 1)
    turtle_obj.left(60)
    draw_branches(turtle_obj, branch_length * 0.7, levels - 1)
    turtle_obj.right(30)
    turtle_obj.backward(branch_length)

# Function to draw leaves of the tree
def draw_leaves(turtle_obj, radius):
    turtle_obj.color("green")
    turtle_obj.penup()
    turtle_obj.goto(turtle_obj.xcor(), turtle_obj.ycor() + radius)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    turtle_obj.circle(radius)
    turtle_obj.end_fill()

# Main function to draw the tree
def main():
    window = turtle.Screen()
    window.bgcolor("white")
    leo = turtle.Turtle()
    leo.speed(0)  # Set the fastest drawing speed
    leo.penup()
    leo.goto(0, -200)
    leo.pendown()

    trunk_height = 100
    trunk_width = 20
    branch_length = 80
    levels = 4
    leaf_radius = 30

    draw_trunk(leo, trunk_height, trunk_width)
    leo.left(90)
    leo.forward(trunk_height)
    draw_branches(leo, branch_length, levels)
    draw_leaves(leo, leaf_radius)

    window.mainloop()

if __name__ == "__main__":
    main()
