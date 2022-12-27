from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import BrickManager
from scoreboard import Scoreboard
import time


STARTING_POSITION = (0, -240)

if __name__ == "__main__":

    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Breakout")
    screen.tracer(0)

    paddle = Paddle(STARTING_POSITION)

    ball = Ball()
    ball.goto(0, -200)

    scoreboard = Scoreboard()

    bricks = BrickManager()
    bricks.create_bricks()

    screen.listen()
    screen.onkey(paddle.go_left, key="Left")
    screen.onkey(paddle.go_right, key="Right")

    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # detect ball reaching the top
        if ball.ycor() > 280:
            scoreboard.you_win()

        # detect collision with brick and remove brick
        for brick in bricks.all_bricks:
            if ball.distance(brick) < 50:
                bricks.all_bricks.remove(brick)
                brick.hideturtle()
                ball.bounce_y()

        # detect collision with left or right wall
        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()

        # detect collision with paddle
        if ball.distance(paddle) < 50 and ball.ycor() > -240:
            ball.bounce_y()
            ball.move_speed += 0.01
            print(ball.move_speed)

        # detect ball passing paddle at bottom of screen
        if ball.ycor() < -280:
            scoreboard.game_over()

    screen.exitonclick()
