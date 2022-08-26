from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0 #player 1 score
        self.r_score = 0 #player 2 score
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 70, "normal"))


