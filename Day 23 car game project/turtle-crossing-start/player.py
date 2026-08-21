STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_forward(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_backward(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
