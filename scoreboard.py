from turtle import Turtle
ALINGMENT = "center"
FONT = ('Courier', 24, 'normal')

with open("data.txt") as file:
    high_score = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.goto(0, 265)
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score

        with open("data.txt", mode="w") as text:
            text.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()