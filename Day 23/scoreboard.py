from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score_board()
        
    def update_score_board(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        
    def next_level(self):
        self.level += 1
        self.update_score_board()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\n You reached Level: {self.level}", align="center", font=FONT)