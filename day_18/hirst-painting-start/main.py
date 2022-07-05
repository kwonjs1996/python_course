import turtle

import colorgram
from turtle import Turtle,Screen
import random
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb_color = (r,g,b)
#     rgb_colors.append(new_rgb_color)
#
# print(rgb_colors)
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")

def random_color():
    color = random.choice(color_list)
    return color

# 10 x 10
# 점 크기 20 점 간격 50


def change_location(x, y):
    tim.up()
    tim.setpos(x, y)


def one_line_dot(times):
    count = 0
    while not count == times:
        x = -250
        y = -250
        for i in range(times):
            change_location(x, y)
            y += 50
            count += 1
            for i in range(times):
                tim.dot(20, random_color())
                tim.penup()
                tim.forward(50)


one_line_dot(10)
tim.hideturtle()


screen = Screen()
screen.exitonclick()