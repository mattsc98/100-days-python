from turtle import Screen
import time

from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    
    #detect colision 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #detect paddle col
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() > -320:
        ball.bounce_x()


screen.exitonclick()