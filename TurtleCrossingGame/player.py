from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.reset()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.setheading(UP)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True

        return False

    def reset(self):
        self.goto(STARTING_POSITION)
