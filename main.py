from turtle import Screen
from spaceship import Spaceship
from aliens import Aliens
import time

screen = Screen()
screen.setup(height=650, width=800)
screen.bgcolor("black")
screen.tracer(0)
ship = Spaceship()
alien = Aliens()

ship.screen.listen()
ship.screen.onkeypress(ship.go_left, "Left")
ship.screen.onkeypress(ship.go_right, "Right")
ship.screen.onkeypress(ship.shoot, "space")

game_is_on = True

last_move = time.time()

while game_is_on:
    screen.update()
    time.sleep(0.02)

    for bullet in ship.bullets:
        bullet.move()
    
    if time.time() - last_move > 2:
        alien.move_aliens()
        last_move = time.time()

screen.mainloop()