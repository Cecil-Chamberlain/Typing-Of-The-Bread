import pygame
import pygame.freetype

pygame.mixer.init()
pygame.freetype.init()

ans = ""

keysdown = set()

key = pygame.mixer.Sound("assets/keyuc.wav")
returnkey = pygame.mixer.Sound("assets/returnuc.wav")

class Text:
    pass

class Answer(Text):
    def __init__(self, x, y, RES):
        self.x = x
        self.y = y
        self.RES = RES
        self.fontsize = int(RES[0]/30)

    def update(self, pressedkeys, questions_set, window, zombies, active_zombies):
        global ans, keysdown
        for event in pressedkeys:
            if event.type == pygame.KEYDOWN:
                key.play()
                if event.key not in keysdown:
                    keysdown.add(event.key)
                    if event.key == pygame.K_RETURN:
                        returnkey.play()
                        for i in active_zombies:
                            if not i.rock:
                                i.check(questions_set, ans)
                        ans = ""
                    elif event.key == pygame.K_BACKSPACE:
                        ans = ans[0:-1]
                    else:
                        ans = ans + event.unicode
            if event.type == pygame.KEYUP:
                keysdown.discard(event.key)

        font = pygame.font.Font(None, self.fontsize)
        answer = font.render(ans + "|", 0, (255,255,255))
        window.blit(answer,(self.x,self.y))
        typeheretext = font.render("Type answer below >", 0, (255,255,255))
        window.blit(typeheretext,(self.x - self.fontsize,self.y-self.fontsize))
