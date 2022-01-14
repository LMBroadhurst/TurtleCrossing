# TODO 1. Create a turtle and screen
# TODO 2. Be able to control the turtles movement
# TODO 3. Generate 'cars' that move left to right across the screen
# TODO 4. Have a loss scenario when a car hits the turtle
# TODO 5. Create a tiered level system that increases difficulty
# TODO 6. Assign a score system to the levels

from turtle import Screen
import time
from player import Player
from cars import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("lightgrey")
screen.title("Turtle Crossing")

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    scoreboard.update_scoreboard()

    car_manager.car_generator()
    car_manager.car_move()

    # turtle + car collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # turtle hits finish line
    if player.ycor() > 290:
        player.reset()
        car_manager.level_up()
        scoreboard.point_scored()

screen.exitonclick()
