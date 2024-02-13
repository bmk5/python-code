import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def get_start_position(self):
        xcor = self.width / 2
        ycor = random.randint(-250, 250)
        return xcor, ycor

    def gen_random_car(self):
        chance = random.randint(0,6)
        if chance <= 1:
            t = Turtle('square')
            t.penup()
            t.color(random.choice(COLORS))
            t.shapesize(stretch_len=2, stretch_wid=1)
            t.goto(self.get_start_position())
            self.cars.append(t)

    def move_cars(self):
        for car in self.cars:
            car.back(self.car_speed)
            if car.xcor() <= -self.width / 2:
                car.hideturtle()
                self.cars.remove(car)

    def collision_with_player(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True

        return False

    def fill_screen(self):
        for i in range(0, 50):
            self.gen_random_car()
            self.move_cars()

    def number_of_cars(self):
        return len(self.cars)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
