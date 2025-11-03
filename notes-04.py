import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("skyblue")

# TMNT - turtles
bleu = turtle.Turtle()
bleu.turtlesize(6)
bleu.color("navy")
bleu.shape("turtle")
bleu.pencolor("lightblue")
bleu.speed(2)
bleu.goto(0, 180)
bleu.begin_fill()
bleu.pendown()
bleu.circle(60)
bleu.goto(0, 120)
bleu.circle(100)
bleu.end_fill()
window.exitonclick()
