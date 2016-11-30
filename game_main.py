import pygame
from sprites import *
from text import *
from questions import *
from death import *


pygame.init()
RES = (800,600)
window = pygame.display.set_mode(RES)
pygame.display.set_caption('Typing Of The Bread')
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT+1, 5000)

PTM = Toastman(RES[0]*0.7,RES[1]*0.5,3300,360,11,"ptmsprite.png", RES, 0.5)
userinput = Answer(RES[0]*0.6,RES[1]*0.2)
Typewriter = Sprites(RES[0]*0.7,RES[1]*0.4,300,360,0,"typewriter.png", RES)
cave_bg1 = Scenery(0,0,3200,RES[1], 0, "cave_bg.png", RES, 1)
cave_bg2 = Scenery(3200, 0, 3200, RES[1], 0, "cave_bg.png", RES, 1)
cave_fg1 = Scenery(0,0,3200,RES[1], 0, "cave_fg.png", RES, 4)
cave_fg2 = Scenery(3200, 0, 3200, RES[1], 0, "cave_fg.png", RES, 4)
ground1 = Scenery(0, 0, 1550, RES[1], 0, "ground.png", RES, 3.5)
ground2 = Scenery(1550, 0, 1550, RES[1], 0, "ground.png", RES, 3.5)
dead = Death(0, 0, RES[0], RES[1], 1, "ded.png")
retry = flash(0, 0, RES[0], RES[1], 1, "restart.png")

level = 0
questions = questions_set[level]
questions = list(questions.keys())

zombies = {}
active_zombies = []
zombie_counter = 0
dead_zombies = []

def spawn_zombie(zombie_counter):
    global zombies
    height = 0
    numbers = set()
    if len(zombies) > zombie_counter:
        for i in range(len(active_zombies)):
            numbers.add(active_zombies[i].number)
        while height in numbers:
            height += 1
        zombies[zombie_counter].number = height
        active_zombies.append(zombies[zombie_counter])
        zombie_counter += 1
    return zombie_counter


for key in range(len(questions)):
    zombies.update({key:Zombie(RES[0]-RES[0]-300,RES[1]*0.53,3300,360,11,"zombie_sprite.png", RES, 0.5, questions[key])})


quitgame = False
while not quitgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame = True
        if event.type == pygame.USEREVENT+1:
            zombie_counter = spawn_zombie(zombie_counter)
    if PTM.life > 0:
        cave_bg1.update(window, RES)
        cave_bg2.update(window, RES)
        ground1.update(window, RES)
        ground2.update(window, RES)
        PTM.update(window, RES)
        Typewriter.update(window, RES)
        for i in active_zombies:
            i.update(window, PTM, RES, dead_zombies)
        for i in dead_zombies:
            if i.dead:
                active_zombies.remove(i)
                dead_zombies.remove(i)
        cave_fg1.update(window, RES)
        cave_fg2.update(window, RES)
        pygame.draw.rect(window, (255,0,0), (RES[0]*0.05,RES[1]*0.05,PTM.life,RES[1]*0.05))
        userinput.update(event, questions_set[level], window, zombies, active_zombies)
    else:
        dead.update(window, RES)
        retry.update(window, RES)
        if event.type == pygame.KEYDOWN:
            zombies = {}
            for key in range(len(questions)):
                zombies.update({key:Zombie(RES[0]-RES[0]-300,RES[1]*0.53,3300,360,11,"zombie_sprite.png", RES, 0.5, questions[key])})
            active_zombies = []
            zombie_counter = 0
            PTM.life = RES[0]*0.9
    pygame.display.flip() # flip-book, update the entire surface all at once.
    #pygame.display.update() # update specific areas specified in the argument.
    clock.tick(30)
    pygame.display.set_caption("fps: " + str(clock.get_fps()))

pygame.quit()  # to uninitialise pygame
quit() # exit from python
