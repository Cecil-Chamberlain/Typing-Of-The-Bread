import pygame
import pygame.freetype
from questions import *
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

    def update(self, window):
        window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
        if (self.pos >= self.frames):
            self.pos = 0
        else:
            self.pos += 1

class Toastman(Sprites):
    life = 100

class Zombie(Sprites):
    
    def __init__(self, x, y, width, height, frames, image, question):
        Sprites.__init__(self, x, y, width, height, frames, image)
        self.question = question
        
    def update(self, window):
        window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
        if (self.pos >= self.frames):
            self.pos = 0
        else:
            self.pos += 1
            self.x += 2
        font = pygame.font.Font(None, 32)
        quest = font.render(self.question, 0, (255,255,255))
        window.blit(quest,(self.x,self.y))
        

    def check(self, text):
        global question_set
        if text == questions_set[0][self.question]:
            zombies[0] = 0
            
