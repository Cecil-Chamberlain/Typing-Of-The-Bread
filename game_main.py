import pygame
from sprites import *

pygame.init()

resolution = (800,600)

window = pygame.display.set_mode(resolution)
pygame.display.set_caption('Typing Of The Bread')

clock = pygame.time.Clock()

PTM = Toastman(resolution[0]*0.5,resolution[1]*0.5,300,360,10,"ptmsprite.png")

quitgame = False
while not quitgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame = True


    window.fill((0,0,0))
    PTM.update(window)

    pygame.display.flip() # flip-book, update the entire surface all at once.
    #pygame.display.update() # update specific areas specified in the argument.
    clock.tick(30)

pygame.quit()  # to uninitialise pygame
quit() # exit from python
