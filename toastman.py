import pygame


class Toastman:
    def __init__(self, x, y, width, height, frames):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.frames = frames
        self.image = pygame.image.load("assets/ptmsprite.png")
        self.pos = 0

    def update(self, window):
        window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
        if (self.pos >= self.frames):
            self.pos = 0
        else:
            self.pos += 1


    
        
