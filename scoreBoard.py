from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt", "r") as file:
            self.high_score = int(file.readline())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_board()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score - 1
            with open("score.txt", "w") as file:
                file.write(str(self.high_score))
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 15, "bold"))

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 15, "bold"))
        self.score += 1
