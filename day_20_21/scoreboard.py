from turtle import Turtle

ALIGN = "center"
FONT = ('arial', 25, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as data_file:
            self.high_score = int(data_file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-50, 270)
        self.score = 0
        self.update_score()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data_file:
                data_file.write(f"{self.high_score}")
        self.score = 0
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGN, font=FONT)
