from turtle import Screen
from myturtle import MyTurtle
from carmanager import CarManager
from levelboard import LevelBoard
import time

def setup_screen():
    screen.setup(width=800, height=600)
    screen.title("Cross the road")
    screen.tracer(0)

def restart_game():
    global game_on, timy, car_manager, level_board

    screen.clear()
    setup_screen()

    timy = MyTurtle()
    car_manager = CarManager()
    level_board = LevelBoard()

    screen.listen()
    screen.onkey(timy.go_up, "Up")
    screen.onkey(timy.go_down, "Down")
    screen.onkey(restart_game, "y")
    screen.onkey(stop_game, "n")

    game_loop(timy, car_manager, level_board)

def stop_game():
    global game_on
    game_on = False
    screen.bye()

def game_loop(timy, car_manager, level_board):
    global game_on
    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move()

        for car in car_manager.all_cars:
            if car.distance(timy) < 20:
                game_on = False
                level_board.lost()
                level_board.ask_restart()
                return

        if timy.finish_line():
            timy.go_to_start()
            car_manager.level_up()
            level_board.level_plus()
            level_board.update_lavel()

        if level_board.level > 3:
            game_on = False
            level_board.win()
            level_board.ask_restart()
            return

screen = Screen()
setup_screen()

timy = MyTurtle()
car_manager = CarManager()
level_board = LevelBoard()

screen.listen()
screen.onkey(timy.go_up, "Up")
screen.onkey(timy.go_down, "Down")
screen.onkey(restart_game, "y")
screen.onkey(stop_game, "n")

game_loop(timy, car_manager, level_board)

screen.exitonclick()

