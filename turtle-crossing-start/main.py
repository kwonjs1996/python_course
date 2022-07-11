import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.tracer(0)
screen.listen()

screen.onkey(key="Up", fun=player.move)

game_is_on = True
counter = 0

while game_is_on:
    time.sleep(player.level_speed)
    screen.update()
    # counter 를 while문 외부에 선언 후 1/6 확률로 create_car() 실행
    if counter == 6:
        car_manager.create_car()
        counter = 0
    for i in range(len(car_manager.cars)):
        if player.distance(car_manager.cars[i]) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() == player.finish_line_y:
        player.level_up()
        scoreboard.level += 1
        scoreboard.update_score()
    counter += 1
    car_manager.move()

screen.exitonclick()

