import random
import turtle
from turtle import Turtle


class Food(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.width = screen_width
        self.height = screen_height

        self.shape('circle')
        self.color('blue')
        self.speed('fastest')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(self.gen_new_position())

    def gen_new_position(self):
        width = int(self.width/2) - 20
        height = int(self.height/2) - 20
        x_cor = random.randint(-width, width)
        y_cor = random.randint(-height, height)
        return x_cor, y_cor



