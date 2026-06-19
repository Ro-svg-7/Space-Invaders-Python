from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-370,305)
    
    def write_score(self):
        self.clear()
        self.write(
            f"Score: {self.score}",
            align="left",
            font=("Arial", 20, "bold")
        )
    def increase_score(self):
        self.score += 1
        self.write_score()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(
            "GAME OVER",
            align="center",
            font=("Arial", 30, "bold")
        )
        self.goto(0,-30)
        self.write(
            f"Your score is: {self.score}",
            align="center",
            font=("Arial", 20, "bold")
        )
    
    def you_win(self):
        self.clear()

        self.goto(0, 20)
        self.write(
            "YOU WIN!",
            align="center",
            font=("Arial", 30, "bold")
        )

        self.goto(0, -30)
        self.write(
            f"Final Score: {self.score}",
            align="center",
            font=("Arial", 20, "normal")
        )