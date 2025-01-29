from time import sleep
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball_ = Ball()
score_board = Scoreboard()

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "s")
screen.onkey(paddle_l.go_down, "x")

game_on = True
def stop_game():
    global game_on
    game_on = False
screen.onkey(stop_game, "q")

try:
    while game_on:
        time.sleep(ball_.move_speed)
        screen.update()
        ball_.move()


        if ball_.ycor() > 280 or ball_.ycor() < -280:
            ball_.bounce_wall()


        if ball_.distance(paddle_l) < 50 or ball_.distance(paddle_r) < 50:
            ball_.bounce_paddle()

        if ball_.xcor() > 380:
            score_board.l_point()
            ball_.reset_position()

        if ball_.xcor() < -380:
            score_board.r_point()
            ball_.reset_position()

        if score_board.r_score == 3:
            score_board.game_over_r()
            screen.update()
            game_on = False
        elif score_board.l_score == 3:
            score_board.game_over_l()
            screen.update()
            game_on = False
except Exception as e:
    print(f"Game ended due to an error: {e}")

print("Game over. Closing the screen...")
time.sleep(5)
screen.bye()

