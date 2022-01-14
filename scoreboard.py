from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.current_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level = {self.current_score}", align="center", font=FONT)

    def point_scored(self):
        self.current_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(" *SPLAT*\nGame Over", align="center", font=FONT)
        
