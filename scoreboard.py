from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lose = "GAME OVER"
        self.win = "YOU WIN"

    def game_over(self):
        self.clear()
        self.goto(0, 230)
        self.write(self.lose, align="center", font=("Courier", 40, "normal"))

    def you_win(self):
        self.clear()
        self.goto(0, 230)
        self.write(self.win, align="center", font=("Courier", 40, "normal"))
