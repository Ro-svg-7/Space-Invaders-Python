from turtle import Turtle

class Alien(Turtle):
    def __init__(self,color, position):
        super().__init__()
        self.shape("turtle")
        self.shapesize(2.5,2.5)
        self.setheading(270)
        self.penup()
        self.color(color)
        self.goto(position)

class Aliens:
    def __init__(self):
        self.all_aliens=[]
        self.create_aliens()
    
    def move_aliens(self):
            for alien in self.all_aliens:
                 alien.goto(alien.xcor(), alien.ycor()-10)

    def create_aliens(self):
        colors = ["#00FF7F", "#00CC66", "#00994C"]

        cols,rows = 12 ,3
        
        start_x, start_y = -330, 180
        px , py = 60, 60

        for row in range(rows):
            for col in range(cols):

                x = start_x + col*px
                y = start_y + row*py

                alien = Alien(colors[row], (x,y))
                self.all_aliens.append(alien)

        


