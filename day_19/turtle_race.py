from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
ready = True
race = False
if user_bet:
    race = True
while race:
    win = True
    while ready:
        x = -240
        y = -180
        for turtle_index in range(0, 6):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(colors[turtle_index])
            new_turtle.penup()
            new_turtle.setpos(x, y)
            y += 30
            all_turtles.append(new_turtle)
        ready = False
    while win:
        for turtle in all_turtles:
            if turtle.xcor() > 220:
                if user_bet == turtle.pencolor():
                    print("You win")
                    win = False
                else:
                    print(f"you lose. {turtle.pencolor()} turtle win!")
                    win = False

            else:
                random_distance = random.randint(0, 10)
                turtle.forward(random_distance)
    race = False

screen.exitonclick()