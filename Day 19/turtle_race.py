from turtle import Turtle, Screen
import random

is_race = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make yo bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

all_turtles = []
start = -120
for color in colors:
    new_t = Turtle("turtle")
    new_t.penup()
    new_t.color(color)
    new_t.goto(x=-230,y=start)
    start += 50
    all_turtles.append(new_t)

if user_bet:
    is_race = True

while(is_race):
    
    for t in all_turtles:
        if(t.xcor() > 230):
            winning_col = t.pencolor()
            if(winning_col == user_bet):
                print(f"You've won! The {winning_col} is the winner")
            else:
                print(f"You've lost! The {winning_col} is the winner")                
           
            is_race = False
        
        rand_distance = random.randint(0, 10)
        t.forward(rand_distance)

screen.exitonclick()