import pygame
import pygame.freetype
from sprites import *

pygame.freetype.init()

ans = ""

keysdown = set()

class Text:
    pass

class Question(Text):
    pass
        
    

class Answer(Text):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, event, window):
        global ans
        global keysdown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # activezombie.answer(ans)
                ans = ""
            elif event.key == pygame.K_BACKSPACE:
                ans = ans[0:-1]
            elif event.key not in keysdown:
                keysdown.add(event.key)
                ans = ans + event.unicode
        if event.type == pygame.KEYUP:
            keysdown.discard(event.key)

        font = pygame.font.Font(None, 32)
        rend = font.render(ans, 0, (255,255,255))
        window.blit(rend,(self.x,self.y))
