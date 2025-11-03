# Turtle Artist
# Author:
# 28 October
# Python3 TurtleArt.py
import turtle

wn = turtle.Screen()
t = turtle.Turtle()


# methods
def spawn_triangles(amount):
    turtle.color("navy blue")
    turtle.goto(0, 0)
    if amount > 0:
        turtle.left(180)
        turtle.forward(100)
        turtle.right(160)
        turtle.forward(20)
        turtle.circle(100, 25)
        spawn_triangles(amount - 1)
    else:
        return


# main code

amount = 8
turtle.pendown()

spawn_triangles(amount)
turtle.color("black")
turtle.goto(0, -50)
turtle.circle(50)
wn.exitonclick()
