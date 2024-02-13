from turtle import Turtle, Screen

my_turtle = Turtle()


def moveTurtle():
    my_turtle.forward(200)
    my_turtle.left(90)


for i in range(0, 4):
    moveTurtle()

my_screen = Screen()
my_screen.exitonclick()
