import random
from turtle import Turtle, Screen

my_turtle = Turtle()


def rand_color():
    red = random.random()
    blue = random.random()
    green = random.random()

    return red, blue, green


def draw_shape(num_sides, side_length):
    angle = 360 / num_sides

    my_turtle.pencolor(rand_color())
    for _ in range(num_sides):
        my_turtle.right(angle)
        my_turtle.forward(side_length)


def main():
    side_length = 100
    num_sides = 3
    while num_sides < 11:
        draw_shape(num_sides, side_length)
        num_sides += 1

    my_screen = Screen()
    my_screen.exitonclick()


main()
