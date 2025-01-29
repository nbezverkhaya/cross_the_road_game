from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    def game_over_r(self):
        self.goto(0, 100)
        self.write("Rights paddle wins!", align="center", font=("Courier", 40, "normal"))
        self.goto(0, 50)
        self.write("Game over. Closing the screen...", align="center", font=("Courier", 40, "normal"))
    def game_over_l(self):
        self.goto(0, 100)
        self.write("Left paddle wins!", align="center", font=("Courier", 40, "normal"))
        self.goto(0, 50)
        self.write("Game over. Closing the screen...", align="center", font=("Courier", 40, "normal"))
