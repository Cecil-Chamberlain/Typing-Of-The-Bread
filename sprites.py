import pygame
import pygame.freetype
from zombies import *

current_zombie = 0

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
        
    

class Zombie(Sprites):
    
    def __init__(self, x, y, width, height, frames, image, question):
        Sprites.__init__(self, x, y, width, height, frames, image)
        self.question = question
        self.notdead = True
        
    def update(self, window, PTM, RES):
        if self.notdead:
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
        else:
            if self.x > (0 - self.width):
                window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
                self.x -= 4
                self.pos = 10
            else:
                pass

    def check(self, questions_set, text):
        global current_zombie
        if text.lower() == questions_set[self.question].lower():
            self.notdead = False

    def kill(self):
        if self.x < (0 - self.width):
            active_zombies.remove(self)
        


class Scenery(Sprites):
    def __init__(self, x, y, width, height, frames, image, speed, RES):
        Sprites.__init__(self, x, y, width, height, frames, image)
        self.speed = speed
        self.RES = RES

    def update(self, window):
        window.blit(self.image,(self.x,self.y))
        if (self.x + self.width) > 0:
            self.x -= self.speed
        else:
            self.x = self.width
