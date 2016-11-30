import pygame

class Death:
    def __init__(self, x, y, width, height, frames, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.frames = frames
        self.image = pygame.image.load("assets/{}".format(image))
        self.pos = 0
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
    def update(self, window, RES):
        window.blit(self.image,(self.x,self.y))

class flash(Death):
   #def __init__(self, x, y, width, height, frames, image):
        #Death.__init__(self, x, y, width, height, frames, image)# note might be redundant
        
    def update(self, window, RES):
        if self.pos > 20:
            self.pos = 0
        if self.pos < 10:
            pygame.draw.rect(window, (0,0,0), (RES[0]*0.02,RES[1]*0.793,RES[0]*0.95,RES[1]*0.10))
            window.blit(self.image,(self.x,self.y))
            self.pos += 1
        else:
            self.pos += 1
            pygame.draw.rect(window, (0,0,0), (RES[0]*0.02,RES[1]*0.793,RES[0]*0.95,RES[1]*0.10))


