from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
score = 0

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.random_create()
        # score += 1
        scoreboard.score += 1
        scoreboard.update_score()
        snake.extend()

    #Detect collision with wall (벽에 뱀이 부딪히는 상황)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 295 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail. (꼬리나 몸통에 부딪히는걸 감지)
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


    # if 헤드 세그먼트가 어떤 세그먼트와든 부딪히면
        #게임 오버


screen.exitonclick()
