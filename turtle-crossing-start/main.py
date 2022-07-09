import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
player = Player()
car_manager = CarManager()
screen.tracer(0)
screen.listen()

screen.onkey(key="Up", fun=player.move)

game_is_on = True
counter = 0
car_manager.cars[0].xcor()
car_manager.cars[0].ycor()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # counter 를 while문 외부에 선언 후 1/6 확률로 create_car() 실행
    if counter == 6:
        car_manager.create_car()
        counter = 0
    counter += 1
    car_manager.move()

