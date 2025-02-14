from turtle import Turtle
FONT = ("Courier", 24, "normal")

class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
    def update_lavel(self):
        self.clear()
        self.goto(-300, 250)
        self.write(f"Level: {self.level}", align="center", font=(FONT)

    def level_plus(self):
        self.level += 1

    def lost(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"You've lost on the {self.level} level :(", align="center", font=("Courier", 40, "normal"))

    def win(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"You've won!", align="center", font=("Courier", 40, "normal"))

    def ask_restart(self):
        self.goto(0, 100)
        self.write("Do you want to play again? (Press 'y')\nFor exit click on the screen or press 'n'.", align="center", font=("Courier", 20, "normal"))
