from turtle import Turtle
ALINGMENT = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 265)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over :(", False, align=ALINGMENT, font=FONT)