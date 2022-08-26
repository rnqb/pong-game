from turtle import Screen, Turtle


class Paddle(Turtle):


    def __init__(ron, position):
        super().__init__()
        ron.goto(position)
        ron.shape("square")
        ron.color("white")
        ron.penup()
        ron.turtlesize(stretch_wid=5, stretch_len=1, outline=None)

    def go_up(ron):
        new_y = ron.ycor() + 50
        ron.goto(ron.xcor(), new_y)

    def go_down(ron):
        new_y = ron.ycor() - 50
        ron.goto(ron.xcor(), new_y)










