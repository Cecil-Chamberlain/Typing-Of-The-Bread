import pygame
import pygame.freetype

pygame.freetype.init()

class Sprites:
    def __init__(self, x, y, width, height, frames, image, RES):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.frames = frames
        self.image = pygame.image.load("assets/{}".format(image))
        self.RES = RES
        self.pos = 0

    def update(self, window, RES):
        window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
        if (self.pos >= self.frames):
            self.pos = 0
        else:
            self.pos += 1



class Toastman(Sprites):
    def __init__(self, x, y, width, height, frames, image, RES, scale):
        Sprites.__init__(self, x, y, width, height, frames, image, RES)
        self.life = RES[0]*0.9
        self.scale = scale
        self.image = pygame.transform.scale(self.image,(int(self.width*scale),int(self.height*scale)))
        self.width = (width/self.frames)*scale
        self.height = height*scale

    def update(self, window, RES):
        if (self.pos >= (self.frames - 1)):
            self.pos = 0
            window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
        else:
            self.pos += 1
            window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
        
    

class Zombie(Sprites):
    
    def __init__(self, x, y, width, height, frames, image, RES, scale, question):
        Sprites.__init__(self, x, y, width, height, frames, image, RES)
        self.scale = scale
        self.question = question
        self.image = pygame.transform.scale(self.image,(int(self.width*scale),int(self.height*scale)))
        self.width = (width/self.frames)*scale
        self.height = height*scale
        self.dying = False
        self.dead = False
        self.number = 0
        self.fontsize = 40*scale
        
        
    def update(self, window, PTM, RES, dead_zombies):
        if not self.dying:
            if (self.pos >= (self.frames -2)):
                self.pos = 0
                window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
            elif (self.x + (self.width*0.6)) > PTM.x:
                self.pos += 1
                PTM.life -= 1
                window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
            else:
                self.pos += 1
                self.x += 2
                window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
            font = pygame.font.Font(None, int(self.fontsize))
            quest = font.render(self.question, 0, (255,255,255))
            window.blit(quest,(self.x + (self.width/2), self.y - (int(self.fontsize) * self.number)))
        else:
            if self.x > (0 - self.width):
                window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
                self.x -= 3.5
                self.pos = 10
            else:
                self.dead = True
                dead_zombies.append(self)

    def check(self, questions_set, text):
        if text.lower() == questions_set[self.question].lower():
            self.dying = True

class Scenery(Sprites):
    def __init__(self, x, y, width, height, frames, image, RES, speed):
        Sprites.__init__(self, x, y, width, height, frames, image, RES)
        self.speed = speed
        self.RES = RES
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

    def update(self, window, RES):
        window.blit(self.image,(self.x,self.y))
        if (self.x + (self.width - 5)) > 0:
            self.x -= self.speed
        else:
            self.x = self.width

class Stationary(Sprites):
    def __init__(self, x, y, width, height, frames, image, RES, scale):
        Sprites.__init__(self, x, y, width, height, frames, image, RES)
        self.RES = RES
        self.scale = scale
        self.image = pygame.transform.scale(self.image,(int(self.width*self.scale),int(self.height*self.scale)))
