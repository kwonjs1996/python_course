from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        self.speed(self.ball_speed)

    def head_direction(self):
        self.setheading(45)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move2(self):
        self.forward(10)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def bounce2(self):
        self.setheading(225)

    def restart(self):
        self.goto(0, 0)
        self.paddle_bounce()
        self.ball_speed = 0.1

