import pgzrun
import random
import time 

WIDTH= 700
HEIGHT= 500

bee = Actor("bee")
flower = Actor("flower")

bee.x = 100
bee.y = 150
msg = "use arow keys to move the bee and touch the flower. " 
score = 0
gameover = False
def draw():
    screen.blit("grass",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text(msg, (100,100))
    screen.draw.text(f"score:{score}",(100,50))
    if gameover:
        screen.fill("white")
        screen.draw.text("You have ran out of time.",(200,200))
        screen.draw.text(f" final score:{score}",(100,50))








pgzrun.go()