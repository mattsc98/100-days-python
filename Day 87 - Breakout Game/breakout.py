import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Breakout")
wn.bgcolor("black")
wn.setup(width=600, height=400)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=4)
paddle.penup()
paddle.goto(0, -180)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

# Bricks
bricks = []

for i in range(3):
    for j in range(6):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color("white")
        brick.penup()
        brick.goto(-250 + j * 100, 150 - i * 30)
        bricks.append(brick)

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 250:
        x = 250
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -250:
        x = -250
    paddle.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1

    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1

    if ball.ycor() < -190:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.ycor() < -170) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-160)
        ball.dy *= -1

    # Ball and brick collisions
    for brick in bricks:
        if brick.distance(ball) < 25:
            brick.hideturtle()
            bricks.remove(brick)
            ball.dy *= -1

    # Check for a win
    if len(bricks) == 0:
        wn.bye()
