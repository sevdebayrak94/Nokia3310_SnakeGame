from turtle import Turtle
from food import Food
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.updatse_score()

    def updatse_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 18, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.updatse_score()



