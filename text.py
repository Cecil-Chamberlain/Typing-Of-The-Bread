import pygame
import pygame.freetype

pygame.freetype.init()

ans = ""

keysdown = set()



class Text:
    pass

class Answer(Text):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, event, questions_set, window, zombies, active_zombies):
        global ans, keysdown
        if event.type == pygame.KEYDOWN:
            if event.key not in keysdown:
                keysdown.add(event.key)
                if event.key == pygame.K_RETURN:
                    for i in active_zombies:
                        i.check(questions_set, ans)
                    ans = ""
                elif event.key == pygame.K_BACKSPACE:
                    ans = ans[0:-1]
                elif event.key == pygame.K_TAB:
                    pass
                else:
                    keysdown.add(event.key)
                    ans = ans + event.unicode
        if event.type == pygame.KEYUP:
            keysdown.discard(event.key)

        font = pygame.font.Font(None, 32)
        rend = font.render(ans, 0, (255,255,255))
        window.blit(rend,(self.x,self.y))
