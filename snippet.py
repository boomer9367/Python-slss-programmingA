import turtle

wn = turtle.Screen()
mikey = turtle.Turtle()

wn.bgcolor("lightgreen")

mikey.color("lightblue")
mikey.pencolor("lightblue")
mikey.fillcolor("lightblue")
mikey.width(5)

mikey.begin_fill()
mikey.circle(100)
mikey.end_fill()
mikey.penup()
mikey.goto(0, 200)
mikey.pd()
mikey.begin_fill()
mikey.circle(80)
mikey.end_fill()
mikey.penup()
mikey.goto(0, 360)
mikey.pd()
mikey.begin_fill()
mikey.circle(60)
mikey.end_fill()

wn.exitonclick()
