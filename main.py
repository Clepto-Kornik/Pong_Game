# Pong Game structure
# 3. random movement of the ball
# 4. collision with wall
# 5. collision with ball
# 6. when player misses
# 7. Score for player 1 and 2


import turtle as t
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)   # turn off animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect paddle missing the ball
    if ball.xcor() > 470:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -470:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
