from turtle import Turtle
from bullets import Bullet

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=4, stretch_wid=1.5)
        self.penup()
        self.goto(0,-280)

        self.bullets = []

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def shoot(self):
        bullet = Bullet(self.xcor(), self.ycor()+20)
        self.bullets.append(bullet)