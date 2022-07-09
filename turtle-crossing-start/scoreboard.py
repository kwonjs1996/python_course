from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-225, 250)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.update_score()
        self.setpos(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)
