import pygame
from sprites import *
from text import *
from questions import *
from death import *

pygame.mixer.pre_init(44100, 16, 2, 128)
pygame.init()
pygame.mixer.init()
RES = (1080,720)
window = pygame.display.set_mode(RES)
pygame.display.set_caption('Typing Of The Bread')
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT+1, 5000)

pygame.mixer.music.load("assets/musicuc.wav")
pygame.mixer.music.play()

rocksound = pygame.mixer.Sound("assets/rocksuc.wav")


PTM = Toastman(RES[0]*0.65,RES[1]*0.5,3300,360,11,"ptmsprite.png", RES, (RES[1]/360) * 0.35)
userinput = Answer(RES[0]*0.8, RES[1]*0.55, RES)
Typewriter = Stationary(RES[0]*0.78,RES[1]*0.6,204,179,0,"typewriter.png", RES, (RES[1]/360) * 0.35)
cave_bg1 = Scenery(0,0,3200,RES[1], 0, "cave_bg.png", RES, 4)
cave_bg2 = Scenery(3200, 0, 3200, RES[1], 0, "cave_bg.png", RES, 4)
cave_fg1 = Scenery(0,0,3200,RES[1], 0, "cave_fg.png", RES, 10)
cave_fg2 = Scenery(3200, 0, 3200, RES[1], 0, "cave_fg.png", RES, 10)
ground1 = Scenery(0, 0, 1550, RES[1], 0, "ground.png", RES, 8)
ground2 = Scenery(1550, 0, 1550, RES[1], 0, "ground.png", RES, 8)
rocks = Rocks(-int(RES[0]*0.6), -int(RES[1]*0.2), int(RES[0]*0.6), int(RES[1]*0.2), 0, "Rockfall2.png", RES, RES[1]//7)
dead = Death(0, 0, RES[0], RES[1], 1, "ded.png")
retry = flash(0, 0, RES[0], RES[1], 1, "restart.png")
win = Death(0, 0, RES[0], RES[1], 1, "survived.png")
final1 = Death(0, 0, RES[0], RES[1], 1, "youWon.png")
final2 = Death(0, 0, RES[0], RES[1], 1, "flunked.png")

level = 0
questions = questions_set[level]
questions = list(questions.keys())

zombies = {}
active_zombies = []
zombie_counter = 0
dead_zombies = []
death_toll = 0
playerscore = 0
modules = 3
shittyprogramming = 0

active_zombies.append(rocks)

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
    zombies.update({key:Zombie(RES[0]-RES[0]-300,RES[1]*0.53,3300,360,11,"zombie_sprite.png", RES, (RES[1]/360) * 0.35, questions[key])})

def printscore(death_toll, totalzombies, ingame, final):
    global playerscore, level, zombie_counter
    if ingame:
        scorefont = pygame.font.Font(None, int(RES[0]*0.05))
        score = scorefont.render("Score : "+str(death_toll)+"/"+str(zombie_counter), 0, (255,255,255))
        window.blit(score,(RES[0]*0.05,RES[1]*0.1))
        runningtotal = scorefont.render("Running Total = "+str(playerscore)+" %",0, (255,255,255))
        window.blit(runningtotal,(RES[0]*0.55,RES[1]*0.1))
    elif final:
        scorefont = pygame.font.Font(None, int(RES[0]*0.05))
        score = scorefont.render("You graduate with "+str(playerscore)+"%", 0, (255,255,255))
        window.blit(score,(RES[0]*0.2,RES[1]*0.7))
    else:
        percent = (100/totalzombies)*death_toll
        scorefont = pygame.font.Font(None, int(RES[0]*0.05))
        score = scorefont.render("You pass module "+str(level+1)+" with "+str(int(percent))+"%", 0, (255,255,255))
        window.blit(score,(RES[0]*0.1,RES[1]*0.5))

def printpass(RES):
    passfont = pygame.font.Font(None, int(RES[0]*0.05))
    passstring = passfont.render("Press Down Arrow To Pass", 0, (255,255,255))
    window.blit(passstring,(RES[0]*0.05,0))
   
quitgame = False
while not quitgame:
    pressedkeys = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame = True
        if event.type == pygame.USEREVENT+1:
            zombie_counter = spawn_zombie(zombie_counter)
        pressedkeys.append(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if active_zombies[0].dead:
                    rocksound.play()
                    active_zombies[0].spawn()
                    for i in active_zombies:
                        if not i.rock and not i.dying and i.x > -RES[0]*0.1:
                            active_zombies.remove(i)
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
                death_toll += 1
        cave_fg1.update(window, RES)
        cave_fg2.update(window, RES)
        printscore(death_toll, len(zombies), True, False)
        userinput.update(pressedkeys, questions_set[level], window, zombies, active_zombies)
    else:
        dead.update(window, RES)
        retry.update(window, RES)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                zombies = {}
                for key in range(len(questions)):
                    zombies.update({key:Zombie(RES[0]-RES[0]-300,RES[1]*0.53,3300,360,11,"zombie_sprite.png", RES, (RES[1]/360) * 0.35, questions[key])})
                active_zombies = []
                zombie_counter = 0
                death_toll = 0
                PTM.life = RES[0]*0.9
                active_zombies.append(rocks)


    if len(active_zombies) == 1 and len(zombies) == zombie_counter:
        if level == len(questions_set) - 1:
            if shittyprogramming == 0:
                percent = (100/len(zombies))*death_toll
                percent = percent/modules
                playerscore = round(percent + playerscore)
                shittyprogramming += 1
            printscore(death_toll, len(zombies), False, True)
            if playerscore > 50:
                final1.update(window, RES)
            else:
                final2.update(window, RES)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    shittyprogramming = 0
                    playerscore = 0
                    level = 0
                    questions = questions_set[level]
                    questions = list(questions.keys())
                    zombies = {}
                    for key in range(len(questions)):
                        zombies.update({key:Zombie(RES[0]-RES[0]-300,RES[1]*0.53,3300,360,11,"zombie_sprite.png", RES, (RES[1]/360) * 0.35, questions[key])})
                    active_zombies = []
                    zombie_counter = 0
                    death_toll = 0
                    PTM.life = RES[0]*0.9
                    active_zombies.append(rocks)
                    ans = ""
            
        else:
            win.update(window, RES)
            printscore(death_toll, len(zombies), False, False)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    percent = (100/len(zombies))*death_toll
                    percent = percent/modules
                    if level == 0:
                        playerscore = round(percent, 2)
                    else:
                        playerscore = round(percent + playerscore, 2)
                    level += 1
                    questions = questions_set[level]
                    questions = list(questions.keys())
                    zombies = {}
                    for key in range(len(questions)):
                        zombies.update({key:Zombie(RES[0]-RES[0]-300,RES[1]*0.53,3300,360,11,"zombie_sprite.png", RES, (RES[1]/360) * 0.35, questions[key])})
                    active_zombies = []
                    zombie_counter = 0
                    death_toll = 0
                    PTM.life = RES[0]*0.9
                    active_zombies.append(rocks)
                    ans = ""

    printpass(RES)
    pygame.draw.rect(window, (255,255,255), (RES[0]*0.045,RES[1]*0.045,PTM.life+RES[0]*0.01,RES[1]*0.06))
    pygame.draw.rect(window, (0,0,0), (RES[0]*0.047,RES[1]*0.047,PTM.life+RES[0]*0.005,RES[1]*0.057))
    pygame.draw.rect(window, (255,0,0), (RES[0]*0.05,RES[1]*0.05,PTM.life,RES[1]*0.05))
    pygame.display.flip() # flip-book, update the entire surface all at once.
    #pygame.display.update() # update specific areas specified in the argument.
    clock.tick(30)
    pygame.display.set_caption("fps: " + str(clock.get_fps()))

pygame.quit()  # to uninitialise pygame
quit() # exit from python
