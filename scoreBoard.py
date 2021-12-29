from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 15, "bold"))

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "bold"))
        self.score += 1
