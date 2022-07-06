from turtle import Turtle

ALIGN = "center"
FONT = ('arial', 25, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-50, 270)
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGN, font=FONT)


    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT)
