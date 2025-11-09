###
# Draw a square
#
import turtle 

def draw_square(length):
    pen = turtle.Turtle()
    pen.speed(5)
    pen.penup()
    pen.goto(0,0)
    pen.pendown()
    for i in range(4):
        pen.forward(length)
        pen.right(90)
    pen.hideturtle()


def draw_triangle(length):
    pen = turtle.Turtle()
    pen.speed(5)
    pen.penup()
    pen.goto(0,0)
    pen.pendown()
    for i in range(3):
        pen.forward(length)
        pen.right(120)
    pen.hideturtle()

def draw_rectangle(length_a,length_b):
    pen = turtle.Turtle()
    pen.speed(5)
    pen.penup()
    pen.goto(0,0)
    pen.pendown()
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)
    pen.hideturtle()




# Create the turtle


# Side length


# Draw a square

# Hide the turtle and finish
