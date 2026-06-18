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

    bullets_to_remove= []
    for bullet in ship.bullets:
        bullet.move()
    
        if bullet.ycor() > 315:
            bullets_to_remove.append(bullet)
            bullet.hideturtle()
            continue
        
        for alien_obj in alien.all_aliens:
            if bullet.distance(alien_obj) < 20:
                bullets_to_remove.append(bullet)
                alien.all_aliens.remove(alien_obj)
                alien_obj.hideturtle()
                bullet.hideturtle()
                break
    
    for bullet in bullets_to_remove:
        if bullet in ship.bullets:
            ship.bullets.remove(bullet)

    if time.time() - last_move > 2:
        alien.move_aliens()
        last_move = time.time()

screen.mainloop()