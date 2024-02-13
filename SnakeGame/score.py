from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')
SCORE_POSITION = (0,270)

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.speed('fastest')
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", True, align= ALIGNMENT, font= FONT)

    def add(self):
        self.score += 1
        self.goto(SCORE_POSITION)
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", True, ALIGNMENT, FONT)
