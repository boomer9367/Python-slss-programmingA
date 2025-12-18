# Recursion
# Author: Justin
# 20 October

# We're drawing trees (recursively)
import turtle

# Create a turtle that draws
wn = turtle.Screen()
t = turtle.Turtle()

# Dictionary to hold colours
LEAF_COLOURS = {
    "spring": "#c28cae",
    "summer": "#a8d4ad",
    "winter": "#92b9bd",
    "fall": "#e57a44",
}


def draw_tree(level: int, branch_length: float):
    """A recursive function to draw trees
    level - the levels of branches
    branch_length - length of branch to draw
    """
    # Base case is when level is 0
    if level == 0:
        # Create a leaf
        t.color(LEAF_COLOURS["spring"])
        t.stamp()
        t.color("brown")
    # For all other levels
    else:
        # 1. Go forward branch_length pixels
        t.forward(branch_length)
        # 2. Turn to the left and draw a -1 level tree
        t.left(37)
        draw_tree(level - 1, branch_length * 0.8)
        # 3. Turn to the right and draw a -1 level tree
        t.right(74)
        draw_tree(level - 1, branch_length * 0.8)
        # 4. Go back to where we started
        t.left(37)  # point north
        t.backward(branch_length)


def draw_complicated_tree(level: int, branch_length: float):
    """A recursive function to draw trees
    level - the levels of branches
    branch_length - length of branch to draw
    """
    # Base case is when level is 0
    if level == 0:
        # Create a leaf
        t.color("darkgreen")
        t.stamp()
        t.color("brown")
    # For all other levels
    else:
        # 1. Go forward branch_length pixels
        t.forward(branch_length)
        # 2. Turn to the left and draw a -1 level tree
        t.left(37)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 3. Turn to the right and draw a -1 level tree
        t.right(74)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 4. Go back to where we started
        t.left(37)  # point north
        draw_complicated_tree(level - 1, branch_length * 0.8)
        t.backward(branch_length)


def factorial(num: int) -> int:
    """Returns the factorial of a given num
    calculated recusrively"""
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1


def fibonacci(num: int) -> int:
    """Returns the nth fibonacci number
    and calculates recursively"""
    # if the number is greater than 2
    # return fibonacci(num - 1) + fibonacci(num - 2)
    # else
    # return 1


# Set up the turtle
t.left(90)
t.color("brown")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(0, -180)
t.pendown()

# # draw_complicated_tree(5, 128)
# print(factorial(3))     # 6
# print(factorial(4))     # 24
# print(factorial(100))   #

# print(fibonacci(5))
# print(fibonacci(1000))

draw_tree(4, 240)

wn.exitonclick()
