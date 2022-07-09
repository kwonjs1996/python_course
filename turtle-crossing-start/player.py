from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.showturtle()
        self.level_speed = 0.1
        self.finish_line_y = FINISH_LINE_Y

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def level_up(self):
        self.setpos(STARTING_POSITION)
        self.level_speed *= 0.5

