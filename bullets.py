from turtle import Turtle

class Bullet(Turtle):
    def __init__(self,x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=0.2, stretch_wid=1.5)
        self.color("yellow")
        self.penup()
        self.goto(x,y)

    def move(self):
        self.goto(self.xcor(), self.ycor()+15)
        