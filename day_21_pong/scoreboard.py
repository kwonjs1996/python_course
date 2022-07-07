from turtle import Turtle

## 200, 250 -200, 250     0,250

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(position)
        self.counting()

    def counting(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("arial", 25, "normal"))
