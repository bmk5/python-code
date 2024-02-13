import random
from turtle import Turtle, Screen


def rand_color():
    red = random.random()
    blue = random.random()
    green = random.random()

    return red, blue, green


def main():
    my_turtle = Turtle()
    my_turtle.speed('fastest')
    deg = 1
    step = 4

    while deg <= 360:
        my_turtle.pencolor(rand_color())
        my_turtle.left(step)
        my_turtle.circle(100)
        deg += step

    my_screen = Screen()
    my_screen.exitonclick()


main()