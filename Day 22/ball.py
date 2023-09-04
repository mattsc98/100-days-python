from turtle import Turtle

START_POS = 0, 0
MOVE_DISTANCE = 5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(START_POS)
        
    def move_ball(self):
        new_x = self.xcor() + MOVE_DISTANCE
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x, new_y)
        

    #add wall colision