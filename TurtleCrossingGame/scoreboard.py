from turtle import Turtle

FONT = ("Courier", 18, "normal")
SCORE_POSITION = (-230, 260)
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.speed('fastest')
        self.level = 1
        self.update_level()

    def update_level(self):
        self.write(f"Level = {self.level}", True, align=ALIGNMENT, font=FONT)

    def add(self):
        self.level += 1
        self.goto(SCORE_POSITION)
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", True, ALIGNMENT, FONT)
