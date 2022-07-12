import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()
lower_states = []
for state in states:
    lower_states.append(state.lower())


def correct_answer(x, y):
    answer_state_t = turtle.Turtle()
    answer_state_t.hideturtle()
    answer_state_t.penup()
    answer_state_t.setpos(answer_x, answer_y)
    answer_state_t.write(arg=f"{answer_state.capitalize()}", move=False, align="center", font=("arial", 10, "normal"))


score = 0

while True:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").lower()
    if answer_state in lower_states or answer_state in states:
        answer_row = data[data.state == answer_state.capitalize()]
        answer_x = int(answer_row.x)
        answer_y = int(answer_row.y)
        score += 1
        correct_answer(answer_x, answer_y)
        # answer_state = turtle.Turtle()
        # answer_state.penup()
        # answer_state.setpos(answer_x, answer_y)

screen.exitonclick()
