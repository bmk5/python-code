import time
from snake import Snake
from food import Food
from score import Score
from turtle import Screen

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title('Snake game')
my_screen.tracer(0)


def has_hit_wall(my_snake):
    width = my_screen.window_width() / 2
    height = my_screen.window_height() / 2
    if (my_snake.xcor() >= width or my_snake.xcor() <= -width
            or my_snake.ycor() >= height or my_snake.ycor() <= -height):
        return True

    return False


snake = Snake()
food = Food(my_screen.window_width(), my_screen.window_height())
score = Score()

my_screen.listen()
my_screen.onkey(key="Up", fun=snake.up)
my_screen.onkey(key="Down", fun=snake.down)
my_screen.onkey(key="Left", fun=snake.left)
my_screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move_forward()

    if snake.has_hit_tail() or has_hit_wall(snake):
        game_is_on = False
        score.game_over()
        continue

    if snake.distance(food) < 15:
        food.goto(food.gen_new_position())
        snake.extend()
        score.add()


my_screen.exitonclick()
