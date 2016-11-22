import pygame
from sprites import *
from text import *
from questions import *
from zombies import *

global zombies

pygame.init()
RES = (800,600)
window = pygame.display.set_mode(RES)
pygame.display.set_caption('Typing Of The Bread')
clock = pygame.time.Clock()
  

PTM = Toastman(RES[0]*0.5,RES[1]*0.3,300,360,10,"ptmsprite.png")
userinput = Answer(RES[0]*0.6,RES[1]*0.2)
Typewriter = Toastman(RES[0]*0.7,RES[1]*0.4,300,360,0,"typewriter.png")

for key in range(len(questions)):
    zombies.append(Zombie(RES[0]-RES[0],RES[1]*0.5,300,360,10,"zombie_sprite.png",questions[key]))

quitgame = False
while not quitgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame = True
        
    
    window.fill((0,0,0))
    PTM.update(window)
    userinput.update(event, window, zombies)
    Typewriter.update(window)
    
    if zombies[0] != 0:
        zombies[0].update(window)
    
    pygame.display.flip() # flip-book, update the entire surface all at once.
    #pygame.display.update() # update specific areas specified in the argument.
    clock.tick(25)
    pygame.display.set_caption("fps: " + str(clock.get_fps()))

pygame.quit()  # to uninitialise pygame
quit() # exit from python
