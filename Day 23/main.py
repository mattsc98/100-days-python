import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Car Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

cars = []
for _ in range(20):
    cars.append(CarManager())

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move_car()
    
    if player.ycor() == 280:
        player.reset_position()
        scoreboard.next_level()




screen.exitonclick()