from turtle import Screen
from spaceship import Spaceship
from aliens import Aliens
from scoreboard import Score
import time

screen = Screen()
screen.setup(height=700, width=800)
screen.bgcolor("black")
screen.tracer(0)
ship = Spaceship()
alien = Aliens()
scoreboard = Score()

def restart():
    global ship, alien, scoreboard, game_is_on
    for alien_obj in alien.all_aliens:
        alien_obj.hideturtle()
    alien = Aliens()
    for bullet in ship.bullets:
        bullet.hideturtle()
    ship.bullets.clear()
    ship.hideturtle()
    ship = Spaceship()
    scoreboard.clear()
    scoreboard = Score()
    ship.screen.onkeypress(ship.go_left, "Left")
    ship.screen.onkeypress(ship.go_right, "Right")
    ship.screen.onkeypress(ship.shoot, "space")
    game_is_on=True


ship.screen.listen()
ship.screen.onkeypress(ship.go_left, "Left")
ship.screen.onkeypress(ship.go_right, "Right")
ship.screen.onkeypress(ship.shoot, "space")
screen.onkeypress(restart, "r")

def get_move_interval():
    remaining = len(alien.all_aliens)
    total = 36
    return max(0.1, 0.8 * (remaining / total))

def play():
    global game_is_on
    last_move = time.time()
    game_is_on = True
    while True:
        if game_is_on:
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
                        alien_obj.health -= 1
                        bullets_to_remove.append(bullet)
                        bullet.hideturtle()
                        break
            
            for bullet in bullets_to_remove:
                if bullet in ship.bullets:
                    ship.bullets.remove(bullet)
            
            for alien_obj in alien.all_aliens:
                if alien_obj.health == 2:
                    alien_obj.color("yellow")
                elif alien_obj.health == 3:
                    alien_obj.color("green")
                else:
                    alien_obj.color("red")
                if alien_obj.health <= 0:
                    alien_obj.hideturtle()
                    alien.all_aliens.remove(alien_obj)
                    scoreboard.increase_score()
                if alien_obj.ycor() < -200:
                    game_is_on = False
                    scoreboard.game_over()
                    break
            
            if len(alien.all_aliens) == 0:
                game_is_on = False
                scoreboard.you_win()
            
            
            if time.time() - last_move > get_move_interval():
                alien.move_aliens()
                last_move = time.time()

play() 

screen.mainloop()