from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    
    #detect colision wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #detect paddle col
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() > -320:
        ball.bounce_x()
        ball.increase_speed()
        
    #detect r paddle miss
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
    
    #detect l paddle miss
    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()