import pygame
from sprites import *
from text import *
from questions import *
from zombies import *


pygame.init()
RES = (800,600)
window = pygame.display.set_mode(RES)
pygame.display.set_caption('Typing Of The Bread')
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT+1, 5000)

PTM = Toastman(RES[0]*0.5,RES[1]*0.3,300,360,10,"ptmsprite.png", RES)
userinput = Answer(RES[0]*0.6,RES[1]*0.2)
Typewriter = Sprites(RES[0]*0.7,RES[1]*0.4,300,360,0,"typewriter.png")
cave_bg1 = Scenery(0,0,3600,RES[1], 0, "cave_bg.png", 2, RES)
cave_bg2 = Scenery(3600, 0, 3600, RES[1], 0, "cave_bg.png", 2, RES)
cave_fg1 = Scenery(0,0,3600,RES[1], 0, "cave_fg.png", 4, RES)
cave_fg2 = Scenery(3600, 0, 3600, RES[1], 0, "cave_fg.png", 4, RES)

for key in range(len(questions)):
    zombies.append(Zombie(RES[0]-RES[0],RES[1]*0.3,300,360,9,"zombie_sprite.png",questions[key]))

active_zombies.append(zombies[0])


quitgame = False
while not quitgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame = True
        if event.type == pygame.USEREVENT+1:
            spawn_zombies()
    
    cave_bg1.update(window)
    cave_bg2.update(window)
    PTM.update(window, RES)
    Typewriter.update(window, RES)
    for i in active_zombies:
        i.update(window, PTM, RES)
    for i in active_zombies:
        i.kill()
    cave_fg1.update(window)
    cave_fg2.update(window)
    pygame.draw.rect(window, (255,0,0), (RES[0]*0.05,RES[1]*0.05,PTM.life,RES[1]*0.05))
    userinput.update(event, questions_set[level], window, current_zombie)


    pygame.display.flip() # flip-book, update the entire surface all at once.
    #pygame.display.update() # update specific areas specified in the argument.
    clock.tick(30)
    pygame.display.set_caption("fps: " + str(clock.get_fps()))

pygame.quit()  # to uninitialise pygame
quit() # exit from python
