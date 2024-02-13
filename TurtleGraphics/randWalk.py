import random
from turtle import Turtle, Screen

headings = [0, 90, 180, 270]


def rand_color():
    red = random.random()
    blue = random.random()
    green = random.random()

    return red, blue, green


def main():
    my_turtle = Turtle()
    my_turtle.pensize(10)
    my_turtle.speed('fast')

    while True:
        my_turtle.pencolor(rand_color())
        my_turtle.setheading(random.choice(headings))
        my_turtle.forward(50)


main()
