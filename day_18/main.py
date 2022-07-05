import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
screen = Screen()
tim.shape("turtle")


def random_color():
    tim.color(random.randint(0, 255),
              random.randint(0, 255),
              random.randint(0, 255))

def draw_figure(agon):
    random_color()
    angle = 360/agon
    for _ in range(agon):
        tim.forward(100)
        tim.right(angle)

def random_walk():
    tim.speed(0)
    for i in range(100):
        tim.width(10)
        coin = random.randrange(0,5)
        if coin == 0:
            tim.right(90)
        elif coin == 1:
            tim.right(180)
        elif coin == 2:
            tim.right(270)
        else:
            tim.right(360)
        tim.forward(30)
        random_color()
def spirogragh(size_of_gap):
    tim.speed(0)
    for i in range(int(360/size_of_gap)):
        tim.circle(150)
        tim.left(size_of_gap)
        random_color()

spirogragh(4)

screen.exitonclick()
