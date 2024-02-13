from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle('square')
        t.fillcolor('white')
        t.speed('fastest')
        t.penup()

        x_cor = position[0] - 20
        y_cor = position[1] - 20
        t.goto(x_cor, y_cor)
        self.segments.append(t)

    def move_segments(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(x=new_x, y=new_y)

    def move_forward(self):
        self.move_segments()
        self.head.forward(MOVE_DISTANCE)

    def move_direction(self, direction):
        self.move_segments()
        self.head.setheading(direction)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.heading() == RIGHT or self.heading() == LEFT:
            self.move_direction(UP)

    def down(self):
        if self.heading() == RIGHT or self.heading() == LEFT:
            self.move_direction(DOWN)

    def left(self):
        if self.heading() == UP or self.heading() == DOWN:
            self.move_direction(LEFT)

    def right(self):
        if self.heading() == UP or self.heading() == DOWN:
            self.move_direction(RIGHT)

    def heading(self):
        return self.head.heading()

    def distance(self, turtle):
        return self.head.distance(turtle)

    def xcor(self):
        return self.head.xcor()

    def ycor(self):
        return self.head.ycor()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def has_hit_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

        return False
