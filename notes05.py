import turtle

bg = turtle.Screen()


def draw_tree(level, branchlength):
    if level < 0:
        turtle.forward(branchlength)

        turtle.left(40)
        draw_tree(level - 1, branchlength / 1.61)

        turtle.left(80)
        draw_tree(level - 1, branchlength / 1.61)

        turtle.left(40)
        turtle.back(branchlength)

    else:
        turtle.color("pink")
        turtle.stamp()
        turtle.color("brown")


turtle.speed(0)
turtle.penup()
turtle.goto(0, -180)
turtle.left(90)
turtle.pendown()

turtle.color("brown")
turtle.width(3)
turtle.shape("triangle")

draw_tree(4, 120)

bg.exitonclick()
