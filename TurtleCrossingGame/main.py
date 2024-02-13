import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


car_manager = CarManager(screen.window_width(), screen.window_height())
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

car_manager.fill_screen()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.gen_random_car()
    car_manager.move_cars()

    if player.is_at_finish():
        player.reset()
        score.add()
        car_manager.level_up()

    if car_manager.collision_with_player(player):
        score.game_over()
        game_is_on = False

    print(f"The number of cars on the screen is {car_manager.number_of_cars()}")

screen.exitonclick()