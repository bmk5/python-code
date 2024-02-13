from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
my_screen = Screen()
my_screen.setup(width=500, height=400)


def run_race(turtles):
    at_finish_line = False

    while not at_finish_line:
        for turtle in turtles:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() >= my_screen.window_width() / 2:
                return turtle


def main():
    turtles = []
    user_bet = my_screen.textinput(title="Make your bet",
                                   prompt="Which turtle is going to win the race? Pick a color").lower()
    y_cor = -80
    for i in range(0, len(colors)):
        t = Turtle(shape="turtle")
        t.fillcolor(colors.pop())
        t.penup()
        t.goto(x=-250, y=y_cor)
        turtles.append(t)
        y_cor += 35

    winner_turtle = run_race(turtles)
    winning_color = winner_turtle.color()[1]

    if winning_color != user_bet:
        print(f"You lose the bet! The {winning_color} turtle won the race")
    else:
        print(f"You won the bet! Your {winning_color} turtle won the race!")


main()
