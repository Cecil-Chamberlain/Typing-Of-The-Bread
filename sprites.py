import pygame
import pygame.freetype

pygame.mixer.init()
pygame.freetype.init()
ding = pygame.mixer.Sound("assets/dinguc.wav")

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
        self.fontsize = 60*scale

    def update(self, window, RES):
        window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
        if (self.pos >= (self.frames - 1)):
            self.pos = 0
        else:
            self.pos += 1
                    
    

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
        self.rock = False
        self.number = 0
        self.fontsize = 50*scale
        
        
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
                self.x += self.scale*10
                window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
            font = pygame.font.Font(None, int(self.fontsize))
            quest = font.render(self.question, 0, (255,255,255))
            window.blit(quest,(self.x + (self.width/2), self.y - (int(self.fontsize) * self.number + self.scale)))
        else:
            if self.x > (0 - self.width):
                window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
                self.x -= 8
                self.pos = 10
            else:
                self.dead = True
                dead_zombies.append(self)

    def check(self, questions_set, text):
        if text.lower() == questions_set[self.question].lower():
            ding.play()
            self.dying = True

class Scenery(Sprites):
    def __init__(self, x, y, width, height, frames, image, RES, speed):
        Sprites.__init__(self, x, y, width, height, frames, image, RES)
        self.speed = speed
        self.RES = RES
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

    def update(self, window, RES):
        window.blit(self.image,(self.x,self.y))
        if (self.x + (self.width - 20)) > 0:
            self.x -= self.speed
        else:
            self.x = self.width

class Rocks(Sprites):
    def __init__(self, x, y, width, height, frames, image, RES, scale):
        Sprites.__init__(self, x, y, width, height, frames, image, RES)
        self.RES = RES
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.dying = True
        self.dead = True
        self.rock = True
        self.number = 0
        self.scale = scale

    def update(self, window, PTM, RES, dead_zombies):
        if not self.dead:
            if (self.y + (self.height)) > RES[1]*0.8:
                self.x -= 8
                window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
            else:
                self.y += self.scale
                window.blit(self.image,(self.x,self.y),(self.pos*self.width,0,self.width,self.height))
            if self.x + self.width < 0:
                self.dead=True

    def spawn(self):
        self.dead= False
        self.x = 0
        self.y = 0

    

class Stationary(Sprites):
    def __init__(self, x, y, width, height, frames, image, RES, scale):
        Sprites.__init__(self, x, y, width, height, frames, image, RES)
        self.RES = RES
        self.scale = scale
        self.image = pygame.transform.scale(self.image,(int(self.width*self.scale),int(self.height*self.scale)))
