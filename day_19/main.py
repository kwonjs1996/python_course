from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(1)
def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_right():
    tim.right(10)
def turn_left():
    tim.left(10)
def clear():
    tim.up()
    tim.clear()
    tim.home()
    tim.down()


screen.listen()
# 함수의 인자로 함수를 전달할 때 함수 뒤에 () 를 붙이지 않는다.
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
