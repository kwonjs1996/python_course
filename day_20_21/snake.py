from turtle import Screen, Turtle

# 상수를 지정 한다. 바꾸면 안될 값이나, 바꾼다면 전체적인 동작 자체가 바뀌는 것들을 상수로 지정한다.
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

## Snake 클래스 내에서 기본적인 init => 초기화? 세팅? 을 시켜준다고 생각하자 가장 기본적인 속성을 부여하는데 사용한다고 생각하자

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # 앞쪽의 블록의 좌표로 이동하게 해서 맨앞의 방향이 틀어져도 따라 갈 수 있게 만든다

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
## setheading()을 사용하면 right()나 left() 함수와는 다르게 현재 보고있는 방향을 기준으로 설정이 되기때문에 다른 조건을 사용하지 않아도
## 되어서 이 상황에 사용하면 좋은 함수였다. 만약 right(),left() 함수를 이용해서 구현하려고 했으면 지금 보고있는 방향을 찾는 if 문을 사용했어야
## 잘 동작했을 것이다. 각 함수마다 if문 한줄 정도가 더 추가 되었어야 한다고 본다.


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)