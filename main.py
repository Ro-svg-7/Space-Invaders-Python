from turtle import Screen
from spaceship import Spaceship
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)
ship = Spaceship()

ship.screen.listen()
ship.screen.onkeypress(ship.go_left, "Left")
ship.screen.onkeypress(ship.go_right, "Right")
ship.screen.onkeypress(ship.shoot, "space")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.02)

    for bullet in ship.bullets:
        bullet.move()

screen.mainloop()