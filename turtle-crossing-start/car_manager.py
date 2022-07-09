from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def create_car(self):
        # random 을 이용해 1/6 확률로 create_car() 실행시키기
        random_chance = random.randint(1, 6)
        # if random_chance == 1:
        new_car = Turtle(shape="square")
        new_car.turtlesize(1, 2)
        new_car.penup()
        new_car.hideturtle()
        new_car.color(f"{random.choice(COLORS)}")
        new_y = random.randint(-250, 250)
        new_car.setpos(300, new_y)
        new_car.showturtle()
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
