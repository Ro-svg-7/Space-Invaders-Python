from turtle import Turtle

class Alien(Turtle):
    def __init__(self,color, position, health):
        super().__init__()
        self.shape("turtle")
        self.shapesize(2.5,2.5)
        self.setheading(270)
        self.penup()
        self.color(color)
        self.goto(position)
        self.health = health

class Aliens:
    def __init__(self):
        self.all_aliens=[]
        self.create_aliens()
    
    def move_aliens(self):
            for alien in self.all_aliens:
                 alien.goto(alien.xcor(), alien.ycor()-15)

    def create_aliens(self):
        colors = ["#00FF7F", "#00CC66", "#00994C"]

        cols,rows = 12 ,3
        
        start_x, start_y = -330, 180
        px , py = 60, 60

        for row in range(rows):
            for col in range(cols):

                x = start_x + col*px
                y = start_y + row*py

                if row == 0:
                    health = 1
                elif row == 1:
                    health= 2
                else:
                    health = 3

                alien = Alien(colors[row], (x,y), health)
                self.all_aliens.append(alien)

        


