from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
        self.penup()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align=ALIGMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGMENT, font=FONT)


