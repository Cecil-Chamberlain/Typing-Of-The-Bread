import pygame
import pygame.freetype
from zombies import *

pygame.freetype.init()

class Sprites:
    def __init__(self, x, y, width, height, frames, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.frames = frames
        self.image = pygame.image.load("assets/{}".format(image))
        self.pos = 0

    def update(self, window, RES):
        window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
        if (self.pos >= self.frames):
            self.pos = 0
        else:
            self.pos += 1

class Toastman(Sprites):
    def __init__(self, x, y, width, height, frames, image, RES):
        Sprites.__init__(self, x, y, width, height, frames, image)
        self.RES = RES
        self.life = RES[0]*0.9

    def update(self, window, RES):
        window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
        if (self.pos >= self.frames):
            self.pos = 0
        else:
            self.pos += 1
        pygame.draw.rect(window, (255,0,0), (RES[0]*0.05,RES[1]*0.05,self.life,RES[1]*0.05))
    

class Zombie(Sprites):
    
    def __init__(self, x, y, width, height, frames, image, question):
        Sprites.__init__(self, x, y, width, height, frames, image)
        self.question = question
        
    def update(self, window, PTM, RES):
        window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
        if (self.pos >= self.frames):
            self.pos = 0
        elif (self.x + self.width) > PTM.x + RES[0]*0.1:
            self.pos += 1
            PTM.life -= 1
        else:
            self.pos += 1
            self.x += 2
        font = pygame.font.Font(None, 32)
        quest = font.render(self.question, 0, (255,255,255))
        window.blit(quest,(self.x,self.y))
        

    def check(self, questions_set, text):
        if text == questions_set[self.question]:
            active_zombies.remove(active_zombies[current_zombie])
            
