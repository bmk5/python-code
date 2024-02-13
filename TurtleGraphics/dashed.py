from turtle import Turtle,Screen

my_turtle = Turtle()

for _ in range (30):
    my_turtle.pendown()
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.forward(5)


my_screen = Screen()
my_screen.exitonclick()