import colorgram, random
from turtle import Turtle, Screen


def extract_colors():
    """Extracts 1000 colors from an image"""
    colors = colorgram.extract('painting.jpeg', 500)
    res = []

    for color in colors:
        res.append(color.rgb)

    return res


def main():
    # setting screen environment
    my_screen = Screen()
    screen_width = my_screen.window_width()
    screen_height = my_screen.window_height()
    my_screen.setworldcoordinates(-1, -1, screen_width - 1, screen_height - 1)
    my_screen.colormode(255)

    # setting turtle(pointer) attributes
    my_turtle = Turtle()
    my_turtle.pensize(10)
    my_turtle.speed('fastest')
    my_turtle.penup()

    # list of color tuples
    colors = extract_colors()

    prev_pos = my_turtle.pos()
    radius = 15
    spacing = 20

    while my_turtle.ycor() < screen_height:
        while my_turtle.xcor() < screen_width:
            my_turtle.dot(radius, random.choice(colors))
            my_turtle.forward(radius + spacing)

        my_turtle.goto(prev_pos[0], prev_pos[1] + radius + spacing)
        prev_pos = my_turtle.pos()

    my_turtle.hideturtle()
    my_screen.exitonclick()


main()
