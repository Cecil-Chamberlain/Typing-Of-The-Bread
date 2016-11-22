import pygame

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
    def update(self, window):
        window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
        if (self.pos >= self.frames):
            self.pos = 0
        else:
            self.pos += 1
            self.x += 2
        if self.x > 400:
            self.__del__()
            

    def __del__(self):
        del self
