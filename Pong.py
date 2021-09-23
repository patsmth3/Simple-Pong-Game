# This is a basic Pong game using the "turtle" module.
# Use w and s to move up and down with the left paddle.
# Use i and k to move up and down with the right paddle.

import turtle
import os


win = turtle.Screen()
win.title("Pong by Pat Smith")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Scoreboard
score_A = 0
score_B = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 18, "normal"))

# Makes the ball move left or right by 2 pixles.
ball.dx = .5
ball.dy = .5


# Function for paddle_a movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# Function for paddle_b movement
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding for paddle_a movement
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")

# keyboard binding for paddle_b movement
win.listen()
win.onkeypress(paddle_b_up, "i")
win.onkeypress(paddle_b_down, "k")

# Main game loop.
while True:
    win.update()

    # Moves the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverses the direction of the ball
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_A, score_B), align="center", font=("Courier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_A, score_B), align="center", font=("Courier", 18, "normal"))

    # Paddle and ball collided
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
