from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    tim.forward(50)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def move_back():
    tim.backward(50)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def turtle_main():
    screen = Screen()
    
    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="d", fun=turn_right)
    screen.onkey(key="s", fun=move_back)
    screen.onkey(key="c", fun=clear)
    
    screen.exitonclick()

turtle_main()