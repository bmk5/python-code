from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()

my_screen.listen()


def move_forward():
    my_turtle.forward(10)


def move_back():
    my_turtle.back(10)


def move_counter_clockwise():
    my_turtle.left(20)


def move_clockwise():
    my_turtle.right(30)


def clear_screen():
    my_screen.resetscreen()


my_screen.onkey(key="W", fun=move_forward)
my_screen.onkey(key="S", fun=move_back)
my_screen.onkey(key="A", fun=move_counter_clockwise)
my_screen.onkey(key="D", fun=move_clockwise)
my_screen.onkey(key="C", fun=clear_screen)

my_screen.exitonclick()
